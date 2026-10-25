# AMO Level-2 · Class 8 · Practice Paper 5
# Each question: ch, scen (unique), stem, opts (correct FIRST), hint, sol, optional fig.


def hist(edges, freqs, top, step, xlab='', bw=46, h=150, ylab=''):
    """Histogram: adjacent bars over class intervals, y axis 0..top with gridlines every step."""
    x0, y0 = 40, 10
    w = len(freqs) * bw
    prims = []
    for v in range(0, top + 1, step):
        y = y0 + h - v * h / top
        prims += [('line', x0, y, x0 + w + 10, y, True, (170, 170, 170), 0.8), ('text', x0 - 16, y, str(v), 10)]
    for i, f in enumerate(freqs):
        x = x0 + i * bw
        prims.append(('rect', x, y0 + h - f * h / top, bw, f * h / top, 'peach'))
        prims.append(('text', x + bw / 2, y0 + h - f * h / top - 8, str(f), 10))
    for i, e in enumerate(edges):
        prims.append(('text', x0 + i * bw, y0 + h + 13, str(e), 10))
    prims += [('line', x0, y0, x0, y0 + h), ('line', x0, y0 + h, x0 + w + 10, y0 + h)]
    if xlab:
        prims.append(('text', x0 + w / 2, y0 + h + 30, xlab, 10))
    if ylab:
        prims.append(('text', x0 + 50, y0 - 16, ylab, 10))
    return prims


def cantor():
    prims = []
    segs = [(0.0, 243.0)]
    for k in range(4):
        y = 14 + k * 26
        for a, b in segs:
            prims.append(('rect', 10 + a, y, b - a, 8, 'grey'))
        prims.append(('text', 290, y + 4, f'Step {k}', 10))
        segs = [s for a, b in segs for s in ((a, a + (b - a) / 3), (b - (b - a) / 3, b))]
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='least square number divisible by 6 8 and 15',
         stem='What is the smallest perfect square that is divisible by each of 6, 8 and 15?',
         opts=['3,600', '120', '14,400', '900'],
         hint='Start from the LCM and make every prime power even.',
         sol='LCM of 6, 8 and 15 = 120 = 2³ × 3 × 5. To make all powers even, multiply by 2 × 3 × 5 = 30: 120 × 30 = 3,600 = 60². (900 is a square but is not divisible by 8.)'),
    dict(ch='1', scen='largest of root 3 1.7 seven quarters and root 3.1',
         stem='Which of these numbers is the largest: √3, 1.7, 7/4, √3.1?',
         opts=['√3.1', '7/4', '√3', '1.7'],
         hint='Compare the squares of the numbers.',
         sol='Squares: √3 → 3, 1.7 → 2.89, 7/4 → 3.0625, √3.1 → 3.1. The largest square is 3.1, so √3.1 is the largest.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='3 to the x plus 1 plus 3 to the x minus 1 equals 270',
         stem='Find x if 3ˣ⁺¹ + 3ˣ⁻¹ = 270.',
         opts=['4', '5', '3', '6'],
         hint='3ˣ⁺¹ = 3 × 3ˣ and 3ˣ⁻¹ = 3ˣ ÷ 3.',
         sol='3 × 3ˣ + 3ˣ/3 = (10/3) × 3ˣ = 270, so 3ˣ = 81 = 3⁴ and x = 4.'),
    dict(ch='2', scen='heartbeats in a year at 72 a minute in standard form',
         stem='A heart beats about 72 times a minute. About how many times does it beat in a year of 365 days? Give the answer in standard form.',
         opts=['3.78 × 10⁷', '3.78 × 10⁶', '6.3 × 10⁵', '2.6 × 10⁸'],
         hint='Minutes in a year = 60 × 24 × 365.',
         sol='Minutes in a year = 5,25,600. 72 × 5,25,600 = 3,78,43,200 ≈ 3.78 × 10⁷. (6.3 × 10⁵ = 72 × 24 × 365 forgets the 60 minutes in each hour.)'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='buy 3 get 1 free against 20 then 5 percent off',
         stem='Shop A offers "buy 3, get 1 free" on identical shirts. Shop B offers 20% off followed by a further 5% off. For a buyer of 4 shirts, which shop gives the larger effective discount, and by how much?',
         opts=['Shop A, by 1 percentage point', 'Shop B, by 1 percentage point', 'Both are equal', 'Shop A, by 5 percentage points'],
         hint='Buy 3 get 1 free means paying for 3 out of 4.',
         sol='Shop A: pay 3/4, a 25% discount. Shop B: 0.8 × 0.95 = 0.76, a 24% discount. Shop A is better by 1 percentage point.'),
    dict(ch='3', scen='borrow ₹8,000 at 9 percent and lend at 12 percent for 2.5 years',
         stem='Sahil borrows ₹8,000 at 9% simple interest and at once lends it at 12% simple interest. How much does he gain in 2.5 years?',
         opts=['₹600', '₹240', '₹1,800', '₹2,400'],
         hint='He gains 3% of ₹8,000 each year.',
         sol='Gain per year = 3% of 8,000 = ₹240. In 2.5 years: 240 × 2.5 = ₹600.'),
    dict(ch='3', scen='salary raised 10 cut 10 then raised 20 percent · net change',
         stem='Nisha\'s salary is raised by 10%, then cut by 10%, and then raised by 20%. What is the overall percentage change from her original salary?',
         opts=['18.8% increase', '20% increase', '10% increase', '21% increase'],
         hint='Multiply the three factors: 1.1, 0.9 and 1.2.',
         sol='1.1 × 0.9 = 0.99 and 0.99 × 1.2 = 1.188. The salary is 118.8% of the original: an 18.8% increase.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='a plus b is 10 and a squared plus b squared is 58 · a minus b squared',
         stem='For numbers a > b, a + b = 10 and a² + b² = 58. What is (a − b)²?',
         opts=['16', '4', '42', '8'],
         hint='(a − b)² + (a + b)² = 2(a² + b²).',
         sol='(a + b)² = 100 = 58 + 2ab, so 2ab = 42. (a − b)² = a² + b² − 2ab = 58 − 42 = 16. (4 is a − b itself; 42 is 2ab.)'),
    dict(ch='4', scen='factor of 4x squared minus 12x plus 9 minus y squared',
         stem='Which of these is a factor of 4x² − 12x + 9 − y²?',
         opts=['2x − 3 + y', '2x + 3 − y', '2x − 9 + y', '4x − 3 − y'],
         hint='4x² − 12x + 9 is a perfect square.',
         sol='4x² − 12x + 9 = (2x − 3)². So the expression is (2x − 3)² − y² = (2x − 3 − y)(2x − 3 + y). A factor is 2x − 3 + y.'),
    dict(ch='4', scen='two-digit number with digit sum 9 increased by 27 when reversed',
         stem='The digits of a two-digit number add up to 9. When the digits are reversed, the number increases by 27. What is the number?',
         opts=['36', '63', '45', '27'],
         hint='Reversing the digits of 10a + b changes the number by 9(b − a).',
         sol='a + b = 9 and 9(b − a) = 27, so b − a = 3. Then b = 6, a = 3, and the number is 36. Check: 63 − 36 = 27.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='25 m pole broken with its top 15 m from the foot · height of the break',
         stem='A 25 m pole breaks at some height, and its top touches the ground 15 m from the foot of the pole. The broken part stays joined at the break. At what height did it break?',
         opts=['8 m', '10 m', '12.5 m', '17 m'],
         hint='If it breaks at height h, the broken part is 25 − h long and is the hypotenuse.',
         sol='(25 − h)² = h² + 15². 625 − 50h + h² = h² + 225, so 50h = 400 and h = 8 m. The broken part is 17 m: 8² + 15² = 17².'),
    dict(ch='5', scen='trapezium with angle A twice angle D and angle B 30 more than angle C',
         stem='In trapezium ABCD, AB is parallel to DC. Angle A is twice angle D, and angle B is 30° more than angle C. What is angle C?',
         opts=['75°', '60°', '105°', '90°'],
         hint='The angles along each slanted side add up to 180°.',
         sol='A + D = 180° with A = 2D gives D = 60°, A = 120°. B + C = 180° with B = C + 30° gives 2C + 30° = 180°, so C = 75°.'),
    dict(ch='5', scen='painted cube cut into 64 small cubes · exactly one face painted',
         stem='A wooden cube is painted on all its faces and then cut into 64 equal small cubes. How many small cubes have paint on exactly one face?',
         opts=['24', '8', '16', '32'],
         hint='The cube is 4 small cubes long on each edge. One-face cubes are in the middle of each face.',
         sol='Each face is a 4 × 4 square of small cubes. The cubes with only that face painted form the inner 2 × 2 block: 4 per face. 6 faces × 4 = 24.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='77 cubes of side 2 cm dropped into a cylinder of radius 7 · rise in water',
         stem='A cylindrical jar of radius 7 cm contains water. 77 metal cubes, each of edge 2 cm, are dropped in and are fully covered by water. By how much does the water level rise? (Take π = 22/7.)',
         opts=['4 cm', '2 cm', '8 cm', '0.4 cm'],
         hint='The volume of the cubes equals πr² × rise.',
         sol='Volume of cubes = 77 × 8 = 616 cm³. Base area = 22/7 × 49 = 154 cm². Rise = 616 ÷ 154 = 4 cm.'),
    dict(ch='6', scen='cone of height 24 cm and volume 1,232 cm³ · total surface area',
         stem='A solid cone is 24 cm tall and has a volume of 1,232 cm³. What is its total surface area? (Take π = 22/7.)',
         opts=['704 cm²', '550 cm²', '858 cm²', '1,232 cm²'],
         hint='Find r from the volume, then the slant height from r and h.',
         sol='(1/3) × 22/7 × r² × 24 = 1,232 gives r² = 49, so r = 7 cm. Slant height = √(7² + 24²) = 25 cm. Total surface = πr(l + r) = 22/7 × 7 × 32 = 704 cm². (550 is only the curved surface.)'),
    dict(ch='6', scen='painting a room with two coats on the ceiling · cost at ₹20 per m² per coat',
         stem='A room is 6 m long, 4 m wide and 3 m high, with a door 2 m × 1 m and a window 1.5 m × 1 m. The four walls (not the door or window) get one coat of paint and the ceiling gets two coats. Paint costs ₹20 per m² for each coat. What is the total cost?',
         opts=['₹2,090', '₹1,610', '₹2,160', '₹1,690'],
         hint='Area of four walls = 2(l + b) × h.',
         sol='Walls = 2(6 + 4) × 3 = 60 m², minus 2 + 1.5 = 56.5 m². Ceiling, two coats: 2 × 24 = 48 m². Total 104.5 m² × ₹20 = ₹2,090. (₹1,610 paints the ceiling only once.)'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='histogram of daily wages · class containing the median',
         fig=drawing(300, 200, hist([100, 150, 200, 250, 300, 350], [6, 10, 16, 12, 6], 16, 2, 'Daily wage (₹)', ylab='Number of workers')),
         stem='The histogram shows the daily wages of the workers in a factory (each class includes its lower value, not its upper value). In which class does the median wage lie?',
         opts=['₹200–250', '₹150–200', '₹250–300', '₹100–150'],
         hint='Find the total, then count bars from the left until you pass the middle worker.',
         sol='Total = 6 + 10 + 16 + 12 + 6 = 50, so the median lies between the 25th and 26th workers. Running totals: 6, 16, 32. The 25th and 26th workers are in the third bar, ₹200–250.'),
    dict(ch='8', scen='teacher joins 30 students then the principal replaces the teacher · principal weight',
         stem='The average weight of 30 students is 40 kg. When their teacher is included, the average rises by 1 kg. When the teacher then leaves and the principal joins instead, the average of the 31 people rises by another 0.5 kg. What is the principal\'s weight?',
         opts=['86.5 kg', '71.5 kg', '72 kg', '101.5 kg'],
         hint='Find the teacher\'s weight first. The principal adds 31 × 0.5 kg to the total.',
         sol='Teacher = 31 × 41 − 30 × 40 = 1,271 − 1,200 = 71 kg. Replacing the teacher raises the total by 31 × 0.5 = 15.5 kg, so the principal weighs 71 + 15.5 = 86.5 kg. (71.5 adds only 0.5 kg.)'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='sold for ₹1,140 at 5 percent loss · extra needed for 5 percent gain',
         stem='A clock sold for ₹1,140 gives a loss of 5%. How much more should it have been sold for to gain 5%?',
         opts=['₹120', '₹114', '₹60', '₹126'],
         hint='₹1,140 is 95% of the cost price.',
         sol='Cost = 1,140 ÷ 0.95 = ₹1,200. For 5% gain: ₹1,260. Extra = 1,260 − 1,140 = ₹120 (10% of the cost, not of ₹1,140).'),
    dict(ch='9', scen='₹2,000 deposited at the start of each of 3 years at 10 percent simple interest',
         stem='Kiara deposits ₹2,000 at the start of each year for 3 years in a scheme paying 10% simple interest a year. How much interest has she earned in total at the end of the third year?',
         opts=['₹1,200', '₹600', '₹1,800', '₹900'],
         hint='The first deposit earns for 3 years, the second for 2 and the third for 1.',
         sol='Interest = 2,000 × 10% × (3 + 2 + 1) = 200 × 6 = ₹1,200.'),
    dict(ch='9', scen='cost ₹600 with 17 percent profit after 10 percent discount · marked price',
         stem='An article costs a shopkeeper ₹600. She marks it so that even after a 10% discount she makes a 17% profit. What is the marked price?',
         opts=['₹780', '₹702', '₹770', '₹800'],
         hint='Selling price = 117% of ₹600, and it is 90% of the marked price.',
         sol='Selling price = 600 × 1.17 = ₹702. Marked price = 702 ÷ 0.9 = ₹780.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='ABCD times 4 equals DCBA',
         stem='In ABCD × 4 = DCBA, each letter is a digit and ABCD is a four-digit number. What is ABCD?',
         opts=['2178', '1089', '2187', '2718'],
         hint='The product is still a four-digit number, so A is small. DCBA ends in A, so A must be even.',
         sol='ABCD × 4 < 10,000, so A ≤ 2; DCBA ends in A, an even digit, so A = 2. D × 4 ends in 2 and D ≥ 8, so D = 8. Working through B and C gives 2178 × 4 = 8712.'),
    dict(ch='10', scen='rectangles in a 4 by 2 grid of squares',
         stem='A rectangle is divided into a grid of 4 columns and 2 rows of equal squares. How many rectangles of all sizes (squares included) can be traced along the grid lines?',
         opts=['30', '8', '20', '18'],
         hint='A rectangle is fixed by choosing 2 of the vertical lines and 2 of the horizontal lines.',
         sol='There are 5 vertical lines and 3 horizontal lines. Pairs of vertical lines: 10. Pairs of horizontal lines: 3. Rectangles = 10 × 3 = 30.'),
    dict(ch='10', scen='smallest number leaving remainder 1 when divided by 2 to 6 and divisible by 7',
         stem='What is the smallest number that leaves a remainder of 1 when divided by 2, 3, 4, 5 or 6, and is divisible by 7?',
         opts=['301', '61', '421', '181'],
         hint='The number is 1 more than a multiple of the LCM of 2, 3, 4, 5 and 6.',
         sol='LCM = 60, so the number is 60k + 1: 61, 121, 181, 241, 301, … Testing for 7: only 301 = 7 × 43 works first.'),
    dict(ch='10', scen='Cantor set total length after step 4 from 81 cm',
         fig=drawing(330, 115, cantor()),
         stem='A line segment 81 cm long has its middle third removed (step 1). At each later step, the middle third of every remaining piece is removed. What is the total length remaining after step 4?',
         opts=['16 cm', '27 cm', '54 cm', '24 cm'],
         hint='Each step keeps 2/3 of the length.',
         sol='After 4 steps: 81 × (2/3)⁴ = 81 × 16/81 = 16 cm, in 16 pieces of 1 cm.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='pairs of positive whole numbers with x squared minus y squared equal to 45',
         stem='How many pairs of positive whole numbers (x, y) satisfy x² − y² = 45?',
         opts=['3', '2', '4', '6'],
         hint='(x − y)(x + y) = 45. Both factors must have the same parity.',
         sol='Factor pairs of 45 with x − y < x + y: 1 × 45, 3 × 15, 5 × 9. All are odd-odd, so each gives whole x and y: (23, 22), (9, 6), (7, 2). That is 3 pairs.'),
    dict(ch='5+10', scen='polyhedron with 12 pentagons and 20 hexagons · vertices',
         stem='A football-shaped polyhedron has 12 pentagonal faces and 20 hexagonal faces. Exactly 3 faces meet at every vertex. How many vertices does it have?',
         opts=['60', '90', '32', '120'],
         hint='Count the corners of all the faces, then remember each vertex is shared by 3 faces.',
         sol='The faces have 12 × 5 + 20 × 6 = 180 corners in all. Each vertex is shared by 3 faces, so V = 180 ÷ 3 = 60. Check with Euler: edges = 180 ÷ 2 = 90, faces = 32, and 32 + 60 − 90 = 2. (90 is the number of edges.)'),
    dict(ch='4+5', scen='rectangle with area x squared plus 7x plus 12 and length x plus 4 at x 5',
         stem='A rectangle has area (x² + 7x + 12) cm² and length (x + 4) cm. What is its perimeter when x = 5?',
         opts=['34 cm', '72 cm', '30 cm', '17 cm'],
         hint='Factorise the area to find the width.',
         sol='x² + 7x + 12 = (x + 3)(x + 4), so the width is (x + 3) cm. At x = 5 the sides are 9 cm and 8 cm, and the perimeter = 2(9 + 8) = 34 cm. (72 is the area.)'),
    dict(ch='3+9', scen='₹12,000 at 8 percent for 2 years then 10 percent for 3 years simple interest',
         stem='₹12,000 is lent at simple interest: 8% a year for the first 2 years and 10% a year for the next 3 years. What is the total interest?',
         opts=['₹5,520', '₹5,400', '₹6,000', '₹4,800'],
         hint='Simple interest is always on the original sum.',
         sol='First 2 years: 12,000 × 16% = ₹1,920. Next 3 years: 12,000 × 30% = ₹3,600. Total ₹5,520.'),
    dict(ch='6+9', scen='ice-cream cones radius 3.5 height 12 filled from a 7.7 litre tub · profit',
         stem='An ice-cream seller fills cones of radius 3.5 cm and height 12 cm (inside measures) from a 7.7 litre tub that cost her ₹1,540. She sells every filled cone for ₹40. What is her profit on the tub? (Take π = 22/7; ignore the cost of the cones.)',
         opts=['₹460', '₹2,000', '₹1,540', '₹500'],
         hint='Find the volume of one cone in cm³; 1 litre = 1,000 cm³.',
         sol='One cone = (1/3) × 22/7 × 3.5 × 3.5 × 12 = 154 cm³. Number of cones = 7,700 ÷ 154 = 50. Takings = 50 × 40 = ₹2,000. Profit = 2,000 − 1,540 = ₹460.'),
]
