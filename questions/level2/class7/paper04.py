# AMO Level-2 · Class 7 · Practice Paper 4
# Each question: ch, scen (unique), stem, opts (correct FIRST), hint, sol, optional fig.


def bars(data, top, step, unit='', bw=34, gap=22, h=150):
    """Bar graph: data = [(label, value)], y axis from 0 to top with gridlines every step."""
    x0, y0 = 40, 10
    w = len(data) * (bw + gap) + gap
    prims = []
    for v in range(0, top + 1, step):
        y = y0 + h - v * h / top
        prims += [('line', x0, y, x0 + w, y, True, (170, 170, 170), 0.8), ('text', x0 - 16, y, str(v), 10)]
    for i, (lab, v) in enumerate(data):
        x = x0 + gap + i * (bw + gap)
        prims += [('rect', x, y0 + h - v * h / top, bw, v * h / top, 'blue'), ('text', x + bw / 2, y0 + h + 14, lab, 10)]
    prims += [('line', x0, y0, x0, y0 + h), ('line', x0, y0 + h, x0 + w, y0 + h)]
    if unit:
        prims.append(('text', x0 + w / 2, y0 + h + 32, unit, 10))
    return prims


def pie(data, r=62):
    """Pie chart: data = [(label, degrees)]; each sector is labelled outside the circle."""
    import math
    cx = cy = r + 50
    fills = ['blue', 'yellow', 'green', 'pink', 'peach', 'lilac']
    prims, a0 = [], -90.0
    for i, (lab, deg) in enumerate(data):
        n = max(4, int(deg / 6))
        pts = [(cx, cy)] + [(cx + r * math.cos(math.radians(a0 + deg * k / n)),
                             cy + r * math.sin(math.radians(a0 + deg * k / n))) for k in range(n + 1)]
        prims.append(('poly', pts, fills[i % len(fills)]))
        m = math.radians(a0 + deg / 2)
        prims.append(('text', cx + (r + 50) * math.cos(m), cy + (r + 16) * math.sin(m), lab, 10))
        a0 += deg
    return prims


def trans(labels):
    """Parallel lines l and m (horizontal) cut by a transversal rising to the right.
    Crossings: A = (150, 40) on l and B = (90, 110) on m. At each crossing the upper-right
    and lower-left angles are acute; labels = [(x, y, text)].
    Label centres that clear the lines: near A use (115, 28) upper-left, (200, 28) upper-right,
    (100, 54) lower-left, (180, 54) lower-right; near B use (58, 98), (140, 98), (40, 122), (122, 122)."""
    prims = [('line', 0, 40, 240, 40), ('line', 0, 110, 240, 110), ('line', 60, 145, 180, 5),
             ('text', 254, 40, 'l', 12), ('text', 254, 110, 'm', 12)]
    return prims + [('text', x, y, t, 11) for x, y, t in labels]


def zig(b_lab, d_lab, e_lab):
    """AB ∥ CD with a bent path B–E–D; the angles at B and D are measured towards A and C."""
    return [('line', 0, 20, 240, 20), ('line', 0, 140, 240, 140), ('line', 40, 20, 190, 80), ('line', 40, 140, 190, 80),
            ('text', 40, 6, 'B', 12), ('text', 236, 6, 'A', 12), ('text', 40, 156, 'D', 12), ('text', 236, 156, 'C', 12),
            ('text', 204, 80, 'E', 12), ('text', 98, 31, b_lab, 11), ('text', 98, 129, d_lab, 11), ('text', 168, 80, e_lab, 11)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='fractions p/60 strictly between 1/4 and 1/3',
         stem='How many fractions of the form p/60, where p is an integer, lie strictly between 1/4 and 1/3?',
         opts=['4', '5', '3', '6'],
         hint='Write 1/4 and 1/3 with denominator 60.',
         sol='1/4 = 15/60 and 1/3 = 20/60. Strictly between them p = 16, 17, 18, 19. That is 4 fractions.'),
    dict(ch='1', scen='(−2/3)(3/5) + 5/2 − (3/5)(1/6)',
         stem='What is the value of (−2/3) × (3/5) + 5/2 − (3/5) × (1/6)?',
         opts=['2', '−2', '12/5', '8/5'],
         hint='Do the two products first, then add using the denominator 10.',
         sol='(−2/3)(3/5) = −2/5 and (3/5)(1/6) = 1/10. So −4/10 + 25/10 − 1/10 = 20/10 = 2.'),
    dict(ch='1', scen='a rational number plus its reciprocal equals 13/6',
         stem='A rational number added to its reciprocal gives 13/6. Which of these could the number be?',
         opts=['3/2', '5/6', '2', '6/13'],
         hint='Test each option: add the number and its reciprocal.',
         sol='3/2 + 2/3 = 9/6 + 4/6 = 13/6. (5/6 + 6/5 = 61/30, 2 + 1/2 = 5/2, 6/13 + 13/6 is far larger.) So 3/2.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='(2⁵ + 2⁵ + 2⁵ + 2⁵) ÷ 4³',
         stem='What is (2⁵ + 2⁵ + 2⁵ + 2⁵) ÷ 4³?',
         opts=['2', '1/2', '4', '8'],
         hint='Adding four equal terms is the same as multiplying by 4 = 2².',
         sol='2⁵ + 2⁵ + 2⁵ + 2⁵ = 4 × 2⁵ = 2⁷. 4³ = 2⁶. 2⁷ ÷ 2⁶ = 2. (Adding powers does not add the exponents.)'),
    dict(ch='2', scen='zeros at the end of 2⁵ × 5³ × 10²',
         stem='How many zeros are at the end of the number 2⁵ × 5³ × 10²?',
         opts=['5', '7', '3', '10'],
         hint='Each zero needs one 2 and one 5.',
         sol='2⁵ × 5³ × 10² = 2⁷ × 5⁵. There are five 5s, so five pairs 2 × 5 and 5 zeros: the number is 2² × 10⁵ = 4,00,000.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='20% profit · with cost 10% less and price ₹18 less profit would be 30%',
         stem='A shopkeeper sells a fan at a 20% profit. If he had bought it for 10% less and sold it for ₹18 less, his profit would have been 30%. What is the cost price?',
         opts=['₹600', '₹540', '₹720', '₹500'],
         hint='Let the cost be x. Write the second selling price in two ways.',
         sol='First selling price: 1.2x. New cost 0.9x, new selling price 1.3 × 0.9x = 1.17x. So 1.2x − 18 = 1.17x, giving 0.03x = 18 and x = ₹600.'),
    dict(ch='3', scen='marks in maths and science · English needed for 85% overall',
         stem='Riya scored 72 out of 90 in Maths and 68 out of 80 in Science. English is out of 50. What must she score in English for her overall percentage in the three subjects to be 85%?',
         opts=['47', '45', '42', '50'],
         hint='Find the total marks needed, not the average of the percentages.',
         sol='Total maximum: 90 + 80 + 50 = 220. 85% of 220 = 187. She has 72 + 68 = 140, so she needs 187 − 140 = 47.'),
    dict(ch='3', scen='buy 3 get 1 free against 25% off for 4 shirts',
         stem='Each shirt costs ₹600. Shop P offers "Buy 3, get 1 free". Shop Q offers 25% off. Kunal needs exactly 4 shirts. Which is cheaper?',
         opts=['Both cost the same', 'Shop P is cheaper', 'Shop Q is cheaper', 'Shop P, by ₹150'],
         hint='Work out the bill at each shop.',
         sol='Shop P: pay for 3 shirts = ₹1,800. Shop Q: 4 × 600 = 2,400, less 25% = ₹1,800. Both cost ₹1,800.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='2-digit number with digit sum 9 increasing by 27 when reversed',
         stem='The digits of a 2-digit number add up to 9. When the digits are reversed, the number increases by 27. What is the number?',
         opts=['36', '63', '45', '27'],
         hint='Let the tens digit be a; the units digit is 9 − a.',
         sol='Number 10a + (9 − a) = 9a + 9. Reversed: 10(9 − a) + a = 90 − 9a. So 90 − 9a − (9a + 9) = 27, giving 81 − 18a = 27 and a = 3. The number is 36 (63 − 36 = 27).'),
    dict(ch='4', scen='(3x² − 5x + 2) − (x² − 2x − 4) + (−x² + x) at x = −2',
         stem='Simplify (3x² − 5x + 2) − (x² − 2x − 4) + (−x² + x) and find its value when x = −2.',
         opts=['14', '6', '−2', '10'],
         hint='When removing the brackets after a minus sign, change every sign inside.',
         sol='3x² − 5x + 2 − x² + 2x + 4 − x² + x = x² − 2x + 6. At x = −2: 4 + 4 + 6 = 14.'),
    dict(ch='4', scen='₹1 ₹2 ₹5 coins in ratio 5 : 3 : 2 worth ₹189',
         stem='A box has ₹1, ₹2 and ₹5 coins in the ratio 5 : 3 : 2 by number. Together they are worth ₹189. How many ₹2 coins are there?',
         opts=['27', '18', '45', '9'],
         hint='Let the numbers be 5x, 3x and 2x. Find the value of each kind.',
         sol='Value: 5x × 1 + 3x × 2 + 2x × 5 = 21x = 189, so x = 9. ₹2 coins: 3 × 9 = 27.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='corresponding angles 2x + 15 and 3x − 20 · the co-interior angle',
         fig=drawing(260, 150, trans([(200, 28, '(2x + 15)°'), (140, 98, '(3x − 20)°')])),
         stem='Lines l and m are parallel and the two marked angles are corresponding angles. What is the size of the angle that is co-interior with the angle marked (3x − 20)°?',
         opts=['95°', '85°', '35°', '105°'],
         hint='Corresponding angles are equal. Co-interior angles add up to 180°.',
         sol='2x + 15 = 3x − 20, so x = 35 and each marked angle is 85°. The co-interior angle is 180° − 85° = 95°.'),
    dict(ch='5', scen='AB ∥ DC with A = 65 and B = 75 · angle C',
         stem='In quadrilateral ABCD, side AB is parallel to side DC. Angle A = 65° and angle B = 75°. What is angle C?',
         opts=['105°', '115°', '75°', '65°'],
         hint='AB ∥ DC, so angles B and C are co-interior.',
         sol='B and C lie between the parallel sides AB and DC on the same side of BC, so B + C = 180° and C = 105°. (Angle D = 115°.)'),
    dict(ch='5', scen='isosceles triangle with vertex angle twice each base angle',
         stem='In an isosceles triangle the vertex angle is twice each base angle. What is the exterior angle at one end of the base?',
         opts=['135°', '90°', '45°', '120°'],
         hint='Let each base angle be x.',
         sol='x + x + 2x = 180, so x = 45°. The exterior angle at a base vertex is 180° − 45° = 135°.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='cuboid volume 4,500 length 25 breadth 12 · surface area',
         stem='A cuboid box has volume 4,500 cm³. Its length is 25 cm and its breadth is 12 cm. What is its total surface area?',
         opts=['1,710 cm²', '855 cm²', '4,500 cm²', '1,350 cm²'],
         hint='Find the height first.',
         sol='Height = 4,500 ÷ 300 = 15 cm. Surface area = 2(25 × 12 + 12 × 15 + 25 × 15) = 2(300 + 180 + 375) = 1,710 cm².'),
    dict(ch='6', scen='cylinders with heights 1 : 2 and radii 2 : 1 · volume ratio',
         stem='The heights of two cylinders are in the ratio 1 : 2 and their radii are in the ratio 2 : 1. What is the ratio of their volumes?',
         opts=['2 : 1', '1 : 2', '4 : 1', '1 : 1'],
         hint='Volume depends on radius × radius × height.',
         sol='Volume ratio = (2 × 2 × 1) : (1 × 1 × 2) = 4 : 2 = 2 : 1.'),
    dict(ch='6', scen='2 cm rain on a 44 m by 35 m roof into a tank of radius 1.4 m',
         stem='During a storm, 2 cm of rain falls on a flat roof 44 m × 35 m. All of it flows into an empty cylindrical tank of radius 1.4 m. How high does the water rise in the tank? (π = 22/7)',
         opts=['5 m', '2.5 m', '10 m', '4 m'],
         hint='Rain volume = roof area × 0.02 m.',
         sol='Rain: 44 × 35 × 0.02 = 30.8 m³. Tank base: 22/7 × 1.4 × 1.4 = 6.16 m². Height = 30.8 ÷ 6.16 = 5 m.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='bar graph of monsoon rainfall · months above the mean',
         fig=drawing(300, 200, bars([('Jun', 120), ('Jul', 280), ('Aug', 240), ('Sep', 160)], 300, 40, 'Rainfall (mm)')),
         stem='The bar graph shows the rainfall in four monsoon months. In how many of these months was the rainfall more than the mean rainfall of the four months?',
         opts=['2', '1', '3', '4'],
         hint='Find the mean first.',
         sol='Mean = (120 + 280 + 240 + 160) ÷ 4 = 800 ÷ 4 = 200 mm. July (280) and August (240) are above 200. That is 2 months.'),
    dict(ch='8', scen='mean minus median of the first ten primes',
         stem='What is the difference between the mean and the median of the first ten prime numbers?',
         opts=['0.9', '1', '0.1', '1.9'],
         hint='List the first ten primes. Remember that 2 is prime.',
         sol='2, 3, 5, 7, 11, 13, 17, 19, 23, 29. Sum 129, so the mean is 12.9. The median is the mean of the 5th and 6th: (11 + 13) ÷ 2 = 12. Difference: 0.9.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='6 taps fill in 4 h · 8 taps for 1 h then 2 closed',
         stem='6 identical taps fill a tank in 4 hours. Leela opens 8 taps, and after 1 hour she closes 2 of them. How long does it take to fill the tank in all?',
         opts=['3 h 40 min', '4 h', '3 h', '4 h 20 min'],
         hint='The tank needs 6 × 4 = 24 tap-hours.',
         sol='First hour: 8 tap-hours. Left: 16 tap-hours with 6 taps = 16/6 h = 2 h 40 min. Total 3 h 40 min.'),
    dict(ch='9', scen='₹1,800 shared 4 : 5 then ₹100 passed from Sita to Gita',
         stem='₹1,800 is shared between Sita and Gita in the ratio 4 : 5. Then Sita gives ₹100 to Gita. What is the new ratio of their money?',
         opts=['7 : 11', '4 : 5', '3 : 4', '8 : 11'],
         hint='Find each share first.',
         sol='Sita ₹800, Gita ₹1,000. After the gift: ₹700 and ₹1,100, a ratio of 7 : 11.'),
    dict(ch='9', scen='late 10 min at 5 km/h and early 5 min at 6 km/h',
         stem='Walking at 5 km/h, Kabir reaches school 10 minutes late. Walking at 6 km/h, he reaches 5 minutes early. How far is the school?',
         opts=['7.5 km', '6 km', '5 km', '9 km'],
         hint='The two walking times differ by 15 minutes = 1/4 hour.',
         sol='d/5 − d/6 = 1/4, so d/30 = 1/4 and d = 7.5 km.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='AB × 9 = A0B',
         stem='A and B are digits and AB is a 2-digit number. AB × 9 = A0B, a 3-digit number with 0 in the middle. What is A + B?',
         opts=['9', '8', '10', '7'],
         hint='Write the equation as (10A + B) × 9 = 100A + B.',
         sol='90A + 9B = 100A + B, so 8B = 10A, that is 4B = 5A. With digits, A = 4 and B = 5: 45 × 9 = 405. A + B = 9.'),
    dict(ch='10', scen='numbers from 1 to 100 divisible by 3 or 5',
         stem='How many whole numbers from 1 to 100 are divisible by 3 or by 5 (or both)?',
         opts=['47', '53', '46', '40'],
         hint='Count multiples of 3, add multiples of 5, then take away those counted twice.',
         sol='Multiples of 3: 33. Multiples of 5: 20. Multiples of 15 (counted twice): 6. 33 + 20 − 6 = 47.'),
    dict(ch='10', scen='1/(1 × 2) + 1/(2 × 3) + … + 1/(9 × 10)',
         stem='What is 1/(1 × 2) + 1/(2 × 3) + 1/(3 × 4) + … + 1/(9 × 10)?',
         opts=['9/10', '1', '10/11', '1/10'],
         hint='1/(1 × 2) = 1 − 1/2 and 1/(2 × 3) = 1/2 − 1/3.',
         sol='Each term 1/(n(n + 1)) = 1/n − 1/(n + 1). Adding, the middle terms cancel: 1 − 1/10 = 9/10.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='number trick multiply by 4 add 6 halve subtract twice the number',
         stem='Om thinks of a number. He multiplies it by 4, adds 6, divides by 2 and then subtracts twice the number he first thought of. What is his final answer?',
         opts=['3', '6', '2', 'It depends on the number'],
         hint='Let the number be x and follow the steps.',
         sol='4x → 4x + 6 → (4x + 6)/2 = 2x + 3 → 2x + 3 − 2x = 3. The answer is always 3.'),
    dict(ch='3+10', scen='percent of 1 to 100 that are squares or cubes',
         stem='What percent of the whole numbers from 1 to 100 are perfect squares or perfect cubes (or both)?',
         opts=['12%', '14%', '10%', '13%'],
         hint='List them; some numbers are both.',
         sol='Squares: 1, 4, 9, …, 100 (10 numbers). Cubes: 1, 8, 27, 64 (4 numbers). 1 and 64 are both. Total 10 + 4 − 2 = 12, which is 12% of 100.'),
    dict(ch='4+9', scen='two classes 5 : 8 · 12 leave each · ratio becomes 2 : 5',
         stem='Two classes have students in the ratio 5 : 8. When 12 students leave each class, the ratio becomes 2 : 5. How many students were there in the two classes at first?',
         opts=['52', '39', '65', '40'],
         hint='Let the classes have 5k and 8k students.',
         sol='(5k − 12) : (8k − 12) = 2 : 5, so 5(5k − 12) = 2(8k − 12). 25k − 60 = 16k − 24, so 9k = 36 and k = 4. The classes had 20 and 32 students: 52 in all.'),
    dict(ch='5+6', scen='two crossing roads 5 m wide in a 60 m by 40 m park',
         stem='A park 60 m × 40 m has two roads, each 5 m wide, crossing at right angles through the middle, parallel to the sides. What is the total area of the roads?',
         opts=['475 m²', '500 m²', '450 m²', '525 m²'],
         hint='The square where the roads cross must not be counted twice.',
         sol='Road along the length: 60 × 5 = 300 m². Road along the width: 40 × 5 = 200 m². The crossing square 5 × 5 = 25 m² is counted twice. Total 475 m².'),
    dict(ch='1+4', scen='(x − 1/2)/(x + 1/3) = 1/2',
         stem='Solve (x − 1/2) ÷ (x + 1/3) = 1/2. What is x?',
         opts=['4/3', '−4/3', '2/3', '5/6'],
         hint='Cross-multiply first.',
         sol='2(x − 1/2) = x + 1/3, so 2x − 1 = x + 1/3 and x = 4/3. Check: (4/3 − 1/2) ÷ (4/3 + 1/3) = (5/6) ÷ (5/3) = 1/2.'),
]
