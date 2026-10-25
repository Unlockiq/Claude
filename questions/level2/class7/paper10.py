# AMO Level-2 · Class 7 · Practice Paper 10
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
    dict(ch='1', scen='students walking cycling bus and 12 by car',
         stem='Of the students in a school, 2/5 walk and 1/3 cycle. Of the rest, 3/4 come by bus and the remaining 12 come by car. How many students are there?',
         opts=['180', '240', '120', '150'],
         hint='Find the fraction of all students who come by car.',
         sol='Walk or cycle: 2/5 + 1/3 = 11/15. Rest: 4/15. By car: 1/4 of 4/15 = 1/15 of all students = 12. Total 180.'),
    dict(ch='1', scen='number which minus 5/12 is 7/18 more than −1/4',
         stem='When 5/12 is subtracted from a rational number, the result is 7/18 more than −1/4. What is the number?',
         opts=['5/9', '−5/9', '1/9', '7/9'],
         hint='Write x − 5/12 = −1/4 + 7/18 and use the denominator 36.',
         sol='−1/4 + 7/18 = −9/36 + 14/36 = 5/36. x = 5/36 + 5/12 = 5/36 + 15/36 = 20/36 = 5/9.'),
    dict(ch='1', scen='sum of reciprocals of −2/3 5/4 and minus the reciprocal of −1/6',
         stem='What is the value of 1 ÷ (−2/3) + 1 ÷ (5/4) − 1 ÷ (−1/6)?',
         opts=['53/10', '−53/10', '7/10', '13/2'],
         hint='Dividing 1 by a fraction gives its reciprocal.',
         sol='−3/2 + 4/5 − (−6) = −15/10 + 8/10 + 60/10 = 53/10.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='(2⁵ × 3⁴) ÷ (6³ × 2²) + 4³ ÷ 2⁵',
         stem='What is (2⁵ × 3⁴) ÷ (6³ × 2²) + 4³ ÷ 2⁵?',
         opts=['5', '3', '6', '7'],
         hint='6³ = 2³ × 3³ and 4³ = 64.',
         sol='Bottom: 2³ × 3³ × 2² = 2⁵ × 3³. The 2⁵ cancels, and 3⁴ ÷ 3³ = 3. Also 4³ ÷ 2⁵ = 64 ÷ 32 = 2. Total: 3 + 2 = 5.'),
    dict(ch='2', scen='heartbeats in a day at 72 per minute',
         stem='A heart beats about 72 times a minute. About how many times does it beat in one day? Give the answer in standard form.',
         opts=['1.0368 × 10⁵', '1.0368 × 10⁴', '4.32 × 10³', '1.728 × 10³'],
         hint='Beats = 72 × 60 × 24.',
         sol='72 × 60 = 4,320 beats an hour (4.32 × 10³). × 24 = 1,03,680 beats a day = 1.0368 × 10⁵. (1.728 × 10³ is 72 × 24, which forgets the minutes.)'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='cost of 20 articles equals selling price of x with 25% profit',
         stem='The cost price of 20 pens equals the selling price of x pens. The profit is 25%. What is x?',
         opts=['16', '15', '25', '18'],
         hint='Each pen sells for 1.25 times its cost.',
         sol='If each pen costs ₹1, it sells for ₹1.25. 20 pens cost ₹20, and 20 ÷ 1.25 = 16 pens sell for ₹20. So x = 16.'),
    dict(ch='3', scen='cost ₹800 marked up 20% then 10% off · profit percent',
         stem='A shopkeeper buys a bag for ₹800. He marks it 20% above his cost and then gives a 10% discount on the marked price. What is his profit percent?',
         opts=['8%', '10%', '12%', '2%'],
         hint='The discount is 10% of the marked price, not of the cost.',
         sol='Marked price: 800 + 160 = ₹960. Discount: 96, so he sells for ₹864. Profit: 64, which is 64/800 = 8%. (10% wrongly subtracts the percentages.)'),
    dict(ch='3', scen='rectangle length up 20% breadth down 20% then length down 10%',
         stem='The length of a rectangle is increased by 20% and its breadth is decreased by 20%. Then its new length is decreased by 10%. By what percent has the area changed overall?',
         opts=['13.6% decrease', '10% decrease', '14% decrease', '4% decrease'],
         hint='Multiply the factors: 1.2, 0.8 and 0.9.',
         sol='1.2 × 0.8 × 0.9 = 0.864, so the new area is 86.4% of the old: a decrease of 13.6%.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='84 split so a third of one part is 7 more than a quarter of the other',
         stem='84 is split into two parts so that one-third of the first part is 7 more than one-quarter of the second part. What is the first part?',
         opts=['48', '36', '42', '54'],
         hint='Let the first part be x; the second is 84 − x.',
         sol='x/3 = (84 − x)/4 + 7. Multiply by 12: 4x = 252 − 3x + 84, so 7x = 336 and x = 48. Check: 48/3 = 16 and 36/4 + 7 = 16.'),
    dict(ch='4', scen='2A − 3B with A = 3x² − 2x + 1 and B = x² + 4x − 3',
         stem='If A = 3x² − 2x + 1 and B = x² + 4x − 3, what is 2A − 3B?',
         opts=['3x² − 16x + 11', '3x² + 8x − 7', '3x² − 16x − 7', '9x² − 16x + 11'],
         hint='Multiply out 2A and 3B, then subtract every term of 3B.',
         sol='2A = 6x² − 4x + 2. 3B = 3x² + 12x − 9. 2A − 3B = 3x² − 16x + 11.'),
    dict(ch='4', scen='train of 20 coaches same capacity with 16 coaches seating 12 more each',
         stem='A train has 20 coaches with the same number of seats. If 4 coaches are removed and each remaining coach gets 12 more seats, the total number of seats is unchanged. How many seats does the train have?',
         opts=['960', '768', '1,200', '1,152'],
         hint='Let each coach have x seats.',
         sol='20x = 16(x + 12), so 4x = 192 and x = 48. Total seats: 20 × 48 = 960.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='alternate angles 5x − 20 and 3x + 20 · obtuse angle at the crossing',
         fig=drawing(260, 150, trans([(100, 54, '(5x − 20)°'), (140, 98, '(3x + 20)°')])),
         stem='Lines l and m are parallel, and the two marked angles are alternate interior angles. What is the obtuse angle formed where the transversal crosses line l?',
         opts=['100°', '80°', '20°', '120°'],
         hint='Alternate angles are equal.',
         sol='5x − 20 = 3x + 20, so x = 20 and each marked angle is 80°. The obtuse angle at that crossing is 180° − 80° = 100°.'),
    dict(ch='5', scen='isosceles triangle with exterior angle 100° at the apex',
         stem='In triangle ABC, AB = AC. Side BA is extended beyond A, and the exterior angle formed at A is 100°. What is angle B?',
         opts=['50°', '80°', '40°', '100°'],
         hint='The exterior angle equals the sum of the two opposite interior angles, which are equal.',
         sol='Exterior angle at A = B + C = 100°. Since AB = AC, B = C = 50°.'),
    dict(ch='5', scen='quadrilateral angles x x + 10 x + 20 x + 30',
         stem='The angles of a quadrilateral are x, x + 10°, x + 20° and x + 30°. What is its largest angle?',
         opts=['105°', '95°', '90°', '120°'],
         hint='The angles add up to 360°.',
         sol='4x + 60 = 360, so x = 75°. The angles are 75°, 85°, 95° and 105°. The largest is 105°.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='cylinder r 7 h 15 poured into a cuboid 22 by 15 base',
         stem='A cylinder of radius 7 cm and height 15 cm is full of water. The water is poured into a cuboid tank with a base 22 cm × 15 cm. How deep is the water in the tank? (π = 22/7)',
         opts=['7 cm', '10 cm', '14 cm', '3.5 cm'],
         hint='The volume of water stays the same.',
         sol='Volume = 22/7 × 7 × 7 × 15 = 2,310 cm³. Depth = 2,310 ÷ (22 × 15) = 2,310 ÷ 330 = 7 cm.'),
    dict(ch='6', scen='matchboxes 4 by 2.5 by 1.5 cm in a 60 by 50 by 30 carton',
         stem='Matchboxes measure 4 cm × 2.5 cm × 1.5 cm. How many fit exactly into a carton 60 cm × 50 cm × 30 cm, all placed the same way?',
         opts=['6,000', '600', '4,500', '7,500'],
         hint='Check how many fit along each edge: 60 ÷ 4, 50 ÷ 2.5, 30 ÷ 1.5.',
         sol='Along the edges: 15, 20 and 20 boxes. Total 15 × 20 × 20 = 6,000. (Volume check: 90,000 ÷ 15 = 6,000.)'),
    dict(ch='6', scen='three 4 cm cubes joined end to end · surface area',
         stem='Three cubes of edge 4 cm are joined end to end to make a cuboid. What is the surface area of the cuboid?',
         opts=['224 cm²', '288 cm²', '192 cm²', '256 cm²'],
         hint='The cuboid is 12 cm × 4 cm × 4 cm. Joining hides some faces.',
         sol='Cuboid 12 × 4 × 4: 2(48 + 48 + 16) = 224 cm². (288 is three separate cubes; joining hides 4 faces of 16 cm².)'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='pie chart of a 24-hour day · sleep minus play and homework',
         fig=drawing(230, 230, pie([('Sleep 120°', 120), ('School 90°', 90), ('Play 45°', 45), ('Homework 30°', 30), ('Others 75°', 75)])),
         stem='The pie chart shows how Ishaan spends a 24-hour day. How many more hours does he sleep than he spends on play and homework together?',
         opts=['3 hours', '5 hours', '6 hours', '2 hours'],
         hint='360° stands for 24 hours, so 15° stands for 1 hour.',
         sol='Sleep: 120 ÷ 15 = 8 h. Play: 3 h. Homework: 2 h. 8 − (3 + 2) = 3 hours.'),
    dict(ch='8', scen='mean 15 of 12 numbers · ×3 then −2 · one value 54 removed',
         stem='The mean of 12 numbers is 15. Each number is multiplied by 3, and then 2 is subtracted from each result. One of the new numbers, 54, is then removed. What is the mean of the 11 numbers left?',
         opts=['42', '43', '41', '40.5'],
         hint='The mean changes in the same way as each number. Then work with the total.',
         sol='New mean: 15 × 3 − 2 = 43, so the 12 new numbers total 12 × 43 = 516. Removing 54 leaves 462. Mean of 11: 462 ÷ 11 = 42.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='a : b = 2 : 3 and b : c = 4 : 5 with a + c = 92',
         stem='If a : b = 2 : 3 and b : c = 4 : 5, and a + c = 92, what is c?',
         opts=['60', '32', '46', '69'],
         hint='Make b the same in both ratios.',
         sol='a : b : c = 8 : 12 : 15, so a : c = 8 : 15. 23 parts = 92, so 1 part = 4 and c = 60.'),
    dict(ch='9', scen='12 taps fill in 7 h · 4 taps closed after 3 h · total time',
         stem='12 taps together fill a tank in 7 hours. After 3 hours, 4 of the taps are closed. How long does it take to fill the tank in all?',
         opts=['9 hours', '10 hours', '8 hours', '6 hours'],
         hint='Count the work in tap-hours: 12 × 7 = 84.',
         sol='First 3 hours: 12 × 3 = 36 tap-hours. Left: 48 tap-hours for 8 taps = 6 hours. Total: 3 + 6 = 9 hours.'),
    dict(ch='9', scen='6 m pole shadow 4.8 m · tree shadow 12 m',
         stem='At the same time of day, a 6 m pole casts a 4.8 m shadow and a tree casts a 12 m shadow. How tall is the tree?',
         opts=['15 m', '9.6 m', '14.4 m', '10 m'],
         hint='Height and shadow length are in the same ratio for both.',
         sol='Height ÷ shadow = 6 ÷ 4.8 = 1.25. Tree = 12 × 1.25 = 15 m.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='AB + B = BA',
         stem='A and B are different digits, and AB and BA are 2-digit numbers. AB + B = BA. What is A × B?',
         opts=['72', '63', '56', '81'],
         hint='Write it as 10A + B + B = 10B + A.',
         sol='10A + 2B = 10B + A, so 9A = 8B. With digits: A = 8, B = 9. Check: 89 + 9 = 98. A × B = 72.'),
    dict(ch='10', scen='pairs from 1 to 10 with an even sum',
         stem='Two different numbers are chosen from 1 to 10. In how many ways can they be chosen so that their sum is even?',
         opts=['20', '25', '45', '10'],
         hint='An even sum needs two odd numbers or two even numbers.',
         sol='Pairs of odd numbers from 1, 3, 5, 7, 9: 10. Pairs of even numbers from 2, 4, 6, 8, 10: 10. Total 20.'),
    dict(ch='10', scen='units digit of 2⁵ × 3⁵ × 7⁵',
         stem='What is the units digit of 2⁵ × 3⁵ × 7⁵?',
         opts=['2', '4', '6', '8'],
         hint='2⁵ × 3⁵ × 7⁵ = 42⁵. Only the units digit matters.',
         sol='42⁵ has the same units digit as 2⁵ = 32, which is 2.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='centre of a 3 by 3 magic square using 1 to 9',
         stem='Lata puts the numbers 1 to 9 in a 3 × 3 grid so that every row, column and diagonal has the same sum. Which number must be in the centre?',
         opts=['5', '9', '15', '1'],
         hint='The magic sum is 45 ÷ 3 = 15. Four lines pass through the centre.',
         sol='The four lines through the centre (middle row, middle column, two diagonals) add to 4 × 15 = 60. They cover all 9 numbers once plus the centre 3 more times: 45 + 3c = 60, so c = 5.'),
    dict(ch='3+10', scen='largest of four percentages of percentages',
         stem='Which is the largest: 30% of 50% of 400, 50% of 30% of 420, 20% of 75% of 380, or 75% of 20% of 410?',
         opts=['50% of 30% of 420', '30% of 50% of 400', '75% of 20% of 410', '20% of 75% of 380'],
         hint='Each one is the same percentage of a different number.',
         sol='30% of 50%, 50% of 30%, 20% of 75% and 75% of 20% all equal 15%. So the largest is the one with the largest number, 420: 15% of 420 = 63 (the others are 60, 61.5 and 57).'),
    dict(ch='4+9', scen='father 4 times son now and twice in 20 years',
         stem='Mukesh is 4 times as old as his son. In 20 years he will be twice as old as his son. How old is Mukesh now?',
         opts=['40', '10', '50', '30'],
         hint='Let the son be x years old. Write both ages in 20 years.',
         sol='In 20 years: 4x + 20 = 2(x + 20) = 2x + 40, so 2x = 20 and x = 10. Mukesh is 4 × 10 = 40.'),
    dict(ch='5+6', scen='rectangular field 5 : 3 with perimeter 320 m · area of a 2 m path inside',
         stem='A rectangular field has its length and breadth in the ratio 5 : 3 and a perimeter of 320 m. A path 2 m wide runs inside the field along all four edges. What is the area of the path?',
         opts=['624 m²', '640 m²', '608 m²', '320 m²'],
         hint='Find the length and breadth first. The inner rectangle is 4 m shorter each way.',
         sol='Length + breadth = 160 m, so the field is 100 m by 60 m (area 6,000 m²). Inside the path: 96 m by 56 m = 5,376 m². Path area: 6,000 − 5,376 = 624 m². (640 m² wrongly takes 2 × 320.)'),
    dict(ch='1+4', scen='x/(−3) + 1/4 = 5/6 − x/2',
         stem='Solve x/(−3) + 1/4 = 5/6 − x/2. What is x?',
         opts=['7/2', '−7/2', '2/7', '13/2'],
         hint='Multiply every term by 12.',
         sol='−4x + 3 = 10 − 6x, so 2x = 7 and x = 7/2.'),
]
