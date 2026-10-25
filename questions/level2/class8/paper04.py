# AMO Level-2 · Class 8 · Practice Paper 4
# Each question: ch, scen (unique), stem, opts (correct FIRST), hint, sol, optional fig.


def line_graph(labels, values, top, step, ylab='', ytitle='', vals=False, dx=60, h=150):
    """Line graph: one point per label, joined by straight lines; y gridlines every step."""
    x0, y0 = 46, 10
    X = lambda i: x0 + 30 + i * dx
    Y = lambda v: y0 + h - v * h / top
    w = 30 + (len(labels) - 1) * dx + 30
    prims = []
    for v in range(0, top + 1, step):
        prims += [('line', x0, Y(v), x0 + w, Y(v), True, (170, 170, 170), 0.8), ('text', x0 - 18, Y(v), str(v), 10)]
    prims.append(('polyline', [(X(i), Y(v)) for i, v in enumerate(values)]))
    prims += [('dot', X(i), Y(v), 3.5) for i, v in enumerate(values)]
    if vals:
        prims += [('text', X(i), Y(v) - 11, str(v), 10) for i, v in enumerate(values)]
    prims += [('text', X(i), y0 + h + 13, lab, 10) for i, lab in enumerate(labels)]
    prims += [('line', x0, y0, x0, y0 + h), ('line', x0, y0 + h, x0 + w, y0 + h)]
    if ylab:
        prims.append(('text', x0 + w / 2, y0 + h + 30, ylab, 10))
    if ytitle:
        prims.append(('text', x0 + 60, y0 - 16, ytitle, 10))
    return prims


def vicsek(n, x, y, s):
    """Vicsek (plus) fractal: keep the centre and the four edge-middle squares of every 3 × 3 split."""
    if n == 0:
        return [('rect', x, y, s, s, 'green')]
    t = s / 3
    out = []
    for i, j in ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)):
        out += vicsek(n - 1, x + i * t, y + j * t, t)
    return out


def vicsek_steps():
    prims = []
    for k, x0 in enumerate((10, 150)):
        prims += [('rect', x0, 10, 108, 108, 'white')] + vicsek(k + 1, x0, 10, 108)
        prims.append(('text', x0 + 54, 132, f'Step {k + 1}', 11))
    return prims


def tri_lines():
    A, B, C = (110, 10), (10, 150), (210, 150)
    P = lambda t, Q: (A[0] + t * (Q[0] - A[0]), A[1] + t * (Q[1] - A[1]))
    D, E = (75, 150), (145, 150)
    return [('poly', [A, B, C], 'yellow'), ('line', *A, *D), ('line', *A, *E),
            ('line', *P(0.5, B), *P(0.5, C))]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='root 1.69 plus root 0.0169 plus root 0.000169',
         stem='What is √1.69 + √0.0169 + √0.000169?',
         opts=['1.443', '1.339', '1.4443', '0.443'],
         hint='√169 = 13. Count decimal places: the square root has half as many.',
         sol='√1.69 = 1.3, √0.0169 = 0.13 and √0.000169 = 0.013. The sum is 1.3 + 0.13 + 0.013 = 1.443.'),
    dict(ch='1', scen='even numbers strictly between 15 squared and 16 squared',
         stem='How many even numbers lie strictly between 15² and 16²?',
         opts=['15', '16', '30', '14'],
         hint='There are 2n numbers strictly between n² and (n + 1)².',
         sol='15² = 225 and 16² = 256. The numbers strictly between are 226 to 255: 30 numbers. The even ones are 226, 228, …, 254, which is (254 − 226) ÷ 2 + 1 = 15.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='zero powers sum minus 2 to the minus 1 times 4 plus 3 to the minus 2 times 9',
         stem='What is (2⁰ + 3⁰ + 4⁰) − (2⁻¹ × 4 + 3⁻² × 9)?',
         opts=['0', '1', '3', '2'],
         hint='Any non-zero number to the power 0 is 1.',
         sol='2⁰ + 3⁰ + 4⁰ = 1 + 1 + 1 = 3. 2⁻¹ × 4 = 2 and 3⁻² × 9 = 1, so the second bracket is 3. 3 − 3 = 0.'),
    dict(ch='2', scen='largest of four small numbers written in different standard forms',
         stem='Which of these numbers is the largest?',
         opts=['0.03 × 10⁻¹', '2.4 × 10⁻³', '290 × 10⁻⁵', '0.0025'],
         hint='Write each one as an ordinary decimal.',
         sol='0.03 × 10⁻¹ = 0.003. 2.4 × 10⁻³ = 0.0024. 290 × 10⁻⁵ = 0.0029. 0.0025 stays. The largest is 0.003.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='₹5,000 item sold at ₹3,400 after 20 percent and an unknown second discount',
         stem='An item marked ₹5,000 is sold for ₹3,400 after two successive discounts. The first discount is 20%. What is the second?',
         opts=['15%', '12%', '18%', '20%'],
         hint='Find the price after the first discount.',
         sol='After 20% off: ₹4,000. The second discount takes it to ₹3,400, a cut of ₹600 on ₹4,000 = 15%. (12% wrongly uses ₹5,000 as the base.)'),
    dict(ch='3', scen='interest 2 years at 6 percent plus 3 years at 9 percent totals ₹1,560',
         stem='A sum is lent at 6% simple interest for 2 years, and the same sum again at 9% for 3 years. The total interest from both is ₹1,560. What is the sum?',
         opts=['₹4,000', '₹3,900', '₹5,200', '₹2,600'],
         hint='Add the percentages: 2 × 6% and 3 × 9%.',
         sol='Total interest = 12% + 27% = 39% of the sum = ₹1,560. Sum = 1,560 × 100 ÷ 39 = ₹4,000.'),
    dict(ch='3', scen='number up 20 percent then down 25 percent ends 54 less',
         stem='A number is increased by 20% and the result is decreased by 25%. The final number is 54 less than the original. What was the original number?',
         opts=['540', '600', '216', '450'],
         hint='1.2 × 0.75 = ?',
         sol='1.2 × 0.75 = 0.9, so the final number is 10% less than the original. 10% of the original is 54, so the original is 540.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='a minus b is 4 and ab is 21 for positive a and b · a plus b',
         stem='Positive numbers a and b satisfy a − b = 4 and ab = 21. What is a + b?',
         opts=['10', '58', '100', '8'],
         hint='(a + b)² = (a − b)² + 4ab.',
         sol='(a + b)² = 16 + 84 = 100, so a + b = 10 (positive). The numbers are 7 and 3.'),
    dict(ch='4', scen='x squared plus 5x minus 24 factorised as x plus p times x plus q',
         stem='x² + 5x − 24 is written as (x + p)(x + q). What is p² + q²?',
         opts=['73', '25', '64', '55'],
         hint='p + q = 5 and pq = −24.',
         sol='Two numbers with sum 5 and product −24 are 8 and −3, so x² + 5x − 24 = (x + 8)(x − 3). p² + q² = 64 + 9 = 73. (Or (p + q)² − 2pq = 25 + 48 = 73.)'),
    dict(ch='4', scen='fraction with denominator 5 more than numerator becoming 3 quarters',
         stem='The denominator of a fraction is 5 more than its numerator. If 3 is added to both, the fraction becomes 3/4. What is the fraction?',
         opts=['12/17', '9/14', '7/12', '15/20'],
         hint='Let the numerator be n. Then (n + 3)/(n + 8) = 3/4.',
         sol='4(n + 3) = 3(n + 8) gives 4n + 12 = 3n + 24, so n = 12. The fraction is 12/17. Check: 15/20 = 3/4.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='right triangle PQR with legs 8 and 15 and point S 6 from Q · PR minus PS',
         stem='In triangle PQR, angle Q = 90°, PQ = 8 cm and QR = 15 cm. Point S lies on QR with QS = 6 cm. What is PR − PS?',
         opts=['7 cm', '5 cm', '9 cm', '10 cm'],
         hint='Use Pythagoras in triangles PQR and PQS.',
         sol='PR = √(64 + 225) = 17 cm. PS = √(64 + 36) = 10 cm. PR − PS = 7 cm.'),
    dict(ch='5', scen='rectangle with angle between diagonals 110 degrees · angle OBC',
         stem='The diagonals of rectangle ABCD meet at O, and angle AOB = 110°. What is angle OBC?',
         opts=['55°', '35°', '70°', '45°'],
         hint='The diagonals of a rectangle are equal and bisect each other, so OA = OB.',
         sol='OA = OB, so triangle AOB is isosceles: angle OBA = (180° − 110°) ÷ 2 = 35°. Angle ABC = 90°, so angle OBC = 90° − 35° = 55°.'),
    dict(ch='5', scen='which pair of facts does not prove two right triangles congruent',
         stem='Two right-angled triangles are being compared. Which of these facts is NOT enough to prove them congruent?',
         opts=['Their two acute angles are equal', 'Hypotenuse and one leg are equal', 'Both legs are equal', 'One leg and the acute angle opposite it are equal'],
         hint='Equal angles alone give the same shape, but not necessarily the same size.',
         sol='Hypotenuse and leg is RHS; both legs is SAS; a leg and its opposite angle (with the right angle) is AAS. Equal angles only show the triangles are similar; one could be larger.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='conical heap of wheat radius 2.1 m height 4 m · volume',
         stem='Wheat is piled in a conical heap of base radius 2.1 m and height 4 m. What is the volume of the wheat? (Take π = 22/7.)',
         opts=['18.48 m³', '55.44 m³', '27.72 m³', '9.24 m³'],
         hint='Volume of a cone = (1/3)πr²h.',
         sol='(1/3) × 22/7 × 2.1 × 2.1 × 4 = (1/3) × 13.86 × 4 = 18.48 m³. (55.44 forgets the 1/3.)'),
    dict(ch='6', scen='road roller diameter 84 cm length 1.2 m for 500 turns · area levelled',
         stem='A road roller is a cylinder of diameter 84 cm and length 1.2 m. How many square metres does it level in 500 complete turns? (Take π = 22/7.)',
         opts=['1,584 m²', '792 m²', '3,168 m²', '158.4 m²'],
         hint='In one turn it levels its curved surface area. Use r = 0.42 m.',
         sol='Curved surface = 2πrh = 2 × 22/7 × 0.42 × 1.2 = 3.168 m². In 500 turns: 1,584 m². (3,168 wrongly uses the diameter as the radius.)'),
    dict(ch='6', scen='4 cm cubes packed in a box 1 m by 40 cm by 20 cm',
         stem='How many cubes of edge 4 cm can be packed into a box measuring 1 m × 40 cm × 20 cm?',
         opts=['1,250', '12,500', '125', '2,000'],
         hint='Count how many fit along each edge.',
         sol='Along 100 cm: 25. Along 40 cm: 10. Along 20 cm: 5. Total = 25 × 10 × 5 = 1,250.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='line graph of monthly sales · greatest rise from the previous month',
         fig=drawing(330, 200, line_graph(['Jan', 'Feb', 'Mar', 'Apr', 'May'], [20, 35, 30, 50, 45], 60, 10, 'Month', ytitle='Sales (thousands of ₹)', vals=True)),
         stem='The line graph shows a shop\'s sales in thousands of rupees. In which month was the rise from the month before the greatest, and by how much?',
         opts=['April, ₹20,000', 'February, ₹15,000', 'April, ₹50,000', 'May, ₹15,000'],
         hint='Look at the change from each month to the next, not at the height.',
         sol='Changes: Feb +15, Mar −5, Apr +20, May −5 (thousands). The greatest rise is in April: ₹20,000.'),
    dict(ch='8', scen='six ordered numbers with two unknown middle values and median 10 · mean',
         stem='The numbers 4, 7, x, x + 2, 15, 19 are in increasing order and their median is 10. What is their mean?',
         opts=['10 5/6', '10', '11', '10 1/2'],
         hint='With six numbers, the median is the average of the 3rd and 4th.',
         sol='Median = (x + x + 2) ÷ 2 = x + 1 = 10, so x = 9. The numbers are 4, 7, 9, 11, 15, 19 with total 65. Mean = 65 ÷ 6 = 10 5/6.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='two items costing ₹1,000 together at 20 percent profit and 10 percent loss gaining ₹50',
         stem='Two items together cost ₹1,000. One is sold at 20% profit and the other at 10% loss, and the overall gain is ₹50. What did the first item cost?',
         opts=['₹500', '₹600', '₹400', '₹750'],
         hint='Let the first cost ₹a; then 0.2a − 0.1(1,000 − a) = 50.',
         sol='0.2a − 100 + 0.1a = 50 gives 0.3a = 150, so a = ₹500. Check: gain 100, loss 50, net ₹50.'),
    dict(ch='9', scen='amount ₹14,400 after 4 years with ₹1,100 interest each year · rate',
         stem='A sum lent at simple interest grows to ₹14,400 in 4 years. The interest each year is ₹1,100. What is the rate of interest?',
         opts=['11%', '7.6%', '12%', '10%'],
         hint='Subtract 4 years of interest to get the sum lent.',
         sol='Interest for 4 years = ₹4,400, so the sum = 14,400 − 4,400 = ₹10,000. Rate = 1,100 ÷ 10,000 × 100 = 11%. (7.6% wrongly divides by ₹14,400.)'),
    dict(ch='9', scen='buying at 20 percent below list and selling at 10 percent above list',
         stem='A dealer buys a television at 20% below its list price and sells it at 10% above the list price. What is her profit percent?',
         opts=['37.5%', '30%', '25%', '32%'],
         hint='Take the list price as ₹100.',
         sol='Cost = ₹80, selling price = ₹110. Profit = 30 on a cost of 80 = 37.5%. (30% wrongly uses the list price as the base.)'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='AA plus BB plus CC equals ABC',
         stem='In AA + BB + CC = ABC, the letters stand for different digits. What is A + B + C?',
         opts=['18', '12', '15', '20'],
         hint='AA + BB + CC = 11(A + B + C). A must be 1.',
         sol='11(A + B + C) is a three-digit number ABC, at most 11 × 24 = 264, so A = 1 or 2. Trying, 11 × 18 = 198 has digits 1, 9, 8 that add to 18. So A + B + C = 18 (11 + 99 + 88 = 198).'),
    dict(ch='10', scen='numbers 1 to 100 divisible by 2 or 3 but not by 6',
         stem='How many numbers from 1 to 100 are divisible by 2 or by 3, but not by 6?',
         opts=['51', '67', '83', '34'],
         hint='Multiples of 6 are counted among the multiples of 2 and also among the multiples of 3.',
         sol='Multiples of 2: 50. Multiples of 3: 33. Multiples of 6: 16. Divisible by 2 but not 6: 50 − 16 = 34. By 3 but not 6: 33 − 16 = 17. Total 51.'),
    dict(ch='10', scen='remainder of 2 to the 50 divided by 7',
         stem='What is the remainder when 2⁵⁰ is divided by 7?',
         opts=['4', '2', '1', '6'],
         hint='Look at the remainders of 2¹, 2², 2³, … when divided by 7.',
         sol='2¹, 2², 2³ leave remainders 2, 4, 1, and the pattern repeats every 3 powers because 2³ = 8 leaves 1. 50 = 3 × 16 + 2, so 2⁵⁰ leaves the same remainder as 2², which is 4.'),
    dict(ch='10', scen='plus-shaped Vicsek fractal · number of small squares after step 3',
         fig=drawing(260, 140, vicsek_steps()),
         stem='A square is split into 9 equal squares and only the centre and the four middle-edge squares are kept (step 1). Each kept square is then treated the same way. Steps 1 and 2 are shown. How many small squares are there after step 3?',
         opts=['125', '45', '243', '25'],
         hint='Each step multiplies the number of squares by 5.',
         sol='Each square becomes 5 smaller squares. Step 1: 5, step 2: 25, step 3: 125.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='two numbers with sum 12 and difference of squares 48 · product',
         stem='Two numbers add up to 12 and the difference of their squares is 48. What is their product?',
         opts=['32', '36', '20', '48'],
         hint='a² − b² = (a + b)(a − b).',
         sol='(a + b)(a − b) = 48 with a + b = 12, so a − b = 4. Then a = 8, b = 4 and the product is 32.'),
    dict(ch='5+10', scen='triangle with two lines from the top and one line across · count triangles',
         fig=drawing(220, 160, tri_lines()),
         stem='A triangle has two lines drawn from its top corner to the base and one line drawn across it, parallel to the base. How many triangles of all sizes are in the figure?',
         opts=['12', '6', '10', '8'],
         hint='Every triangle has the top corner and a base on one of the two horizontal lines.',
         sol='From the top there are 4 lines going down. Any 2 of them, together with one horizontal line, make a triangle. Pairs of lines: 6. Horizontal lines: 2. Total 6 × 2 = 12.'),
    dict(ch='4+5', scen='right triangle with legs x and x plus 7 and hypotenuse 13 · area',
         stem='A right-angled triangle has legs x cm and (x + 7) cm and hypotenuse 13 cm. What is its area?',
         opts=['30 cm²', '60 cm²', '65 cm²', '42 cm²'],
         hint='Try whole-number values of x.',
         sol='We need x² + (x + 7)² = 169. Trying x = 5: 25 + 144 = 169. So the legs are 5 cm and 12 cm, and the area = ½ × 5 × 12 = 30 cm². (60 forgets the ½.)'),
    dict(ch='3+9', scen='rice price falls 20 percent letting ₹600 buy 5 kg more · original price',
         stem='The price of rice falls by 20%. Now ₹600 buys 5 kg more rice than before. What was the original price per kg?',
         opts=['₹30', '₹24', '₹25', '₹36'],
         hint='The ₹600 now buys as much as ₹750 would have bought before.',
         sol='At 80% of the price, ₹600 buys what ₹750 bought before. So the extra 5 kg is worth ₹150 at the old price: ₹30 per kg. (₹24 is the new price.)'),
    dict(ch='6+9', scen='cylindrical tank radius 1.4 m height 2.5 m used at 616 litres a day',
         stem='A cylindrical tank of radius 1.4 m and height 2.5 m is full. A family uses 616 litres of water a day. For how many days will the water last? (Take π = 22/7.)',
         opts=['25 days', '20 days', '2.5 days', '250 days'],
         hint='1 m³ = 1,000 litres.',
         sol='Volume = 22/7 × 1.4 × 1.4 × 2.5 = 15.4 m³ = 15,400 litres. 15,400 ÷ 616 = 25 days.'),
]
