# AMO Level-2 · Class 5 · Practice Paper 2  (format: see paper01.py)


def pict(rows, em, key, lw=90, step=28):
    """Pictograph: one row of symbols per label, then the key."""
    prims = []
    for i, (lab, n) in enumerate(rows):
        y = 18 + i * 34
        prims += [('rect', 0, y - 15, lw, 30, 'lilac'), ('text', lw / 2, y, lab, 12)]
        prims += [('emoji', em, lw + 20 + k * step, y, 24) for k in range(n)]
    y = 18 + len(rows) * 34 + 6
    prims += [('emoji', em, 14, y, 20), ('text', 40 + len(key) * 3.6, y, '= ' + key, 12)]
    return prims


def l_shape():
    s = 12
    P = lambda x, y: (10 + x * s, 10 + y * s)
    return [('poly', [P(0, 0), P(8, 0), P(8, 5), P(12, 5), P(12, 10), P(0, 10)], 'green'),
            ('text', *P(4, -0.8), '8 cm', 11), ('text', *P(-1.8, 5), '10 cm', 11), ('text', *P(6, 10.9), '12 cm', 11),
            ('text', *P(13.6, 7.5), '5 cm', 11), ('text', *P(10, 4.2), '4 cm', 11), ('text', *P(9.4, 2.5), '5 cm', 11)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='numbers from 1 to 100 that are multiples of 4 or 6',
         stem='How many numbers from 1 to 100 are multiples of 4 or of 6 (or of both)?',
         opts=['33', '41', '25', '29'],
         hint='Numbers that are multiples of both 4 and 6 are multiples of 12. Do not count them twice.',
         sol='Multiples of 4: 25 (4 to 100). Multiples of 6: 16 (6 to 96). Multiples of 12 are in both lists: 8 (12 to 96). 25 + 16 − 8 = 33. (41 counts the multiples of 12 twice.)'),
    dict(ch='1', scen='swap the lakhs digit and the tens digit of 7,48,592',
         stem='Tara swaps the lakhs digit and the tens digit of 7,48,592. By how much does the number increase?',
         opts=['1,99,980', '2,00,020', '1,99,800', '2,00,000'],
         hint='Write the new number first.',
         sol='The lakhs digit is 7 and the tens digit is 9. After swapping: 9,48,572. 9,48,572 − 7,48,592 = 1,99,980.'),
    dict(ch='1', scen='which of 36 48 40 45 has the most factors',
         stem='Which of these numbers has the most factors: 36, 48, 40 or 45?',
         opts=['48', '36', '40', '45'],
         hint='List the factors in pairs.',
         sol='36: 1, 2, 3, 4, 6, 9, 12, 18, 36 (9 factors). 48: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48 (10). 40: 1, 2, 4, 5, 8, 10, 20, 40 (8). 45: 1, 3, 5, 9, 15, 45 (6). So 48.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='missing sign in 48 divided by bracket 6 box 2 plus 5 times 3 equals 21',
         fig=equations([['48 ÷ (6 ? 2) + 5 × 3', '=', '21']], size=28),
         stem='Which sign should replace the question mark to make this true?',
         opts=['+', '−', '×', '÷'],
         hint='5 × 3 = 15, so 48 ÷ (6 ? 2) must be 6.',
         sol='5 × 3 = 15, so 48 ÷ (6 ? 2) must be 21 − 15 = 6. 48 ÷ 8 = 6, and 6 + 2 = 8. The sign is +. (− gives 27, × gives 19, ÷ gives 31.)'),
    dict(ch='2', scen='rounding four prices to the nearest ₹10 · estimate minus exact',
         stem='Nitin rounds each of these prices to the nearest ₹10 and adds them: ₹347, ₹582, ₹119 and ₹265. By how much is his estimate more than the exact total?',
         opts=['₹7', '₹3', '₹13', '₹17'],
         hint='Compare each rounded price with the real price.',
         sol='Rounded: 350 + 580 + 120 + 270 = ₹1,320. Exact: 347 + 582 + 119 + 265 = ₹1,313. The estimate is ₹7 more. (The changes are +3, −2, +1, +5.)'),
    dict(ch='2', scen='25 boxes of 24 packets of 36 biscuits',
         stem='A box holds 24 packets and each packet has 36 biscuits. Shalini fills 25 such boxes. How many biscuits is that?',
         opts=['21,600', '2,160', '21,000', '22,600'],
         hint='Multiply 24 × 25 first.',
         sol='Biscuits = 25 × 24 × 36. 25 × 24 = 600, and 600 × 36 = 21,600.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='60 students 40 percent girls · glasses among girls and boys',
         stem='A class has 60 students and 40% of them are girls. Half of the girls and 25% of the boys wear glasses. How many students wear glasses?',
         opts=['21', '30', '15', '24'],
         hint='First find the number of girls and boys.',
         sol='Girls: 40% of 60 = 24, so boys = 36. Girls with glasses: 12. Boys with glasses: 25% of 36 = 9. Total 12 + 9 = 21.'),
    dict(ch='3', scen='3/4 plus 0.6 plus 7/20 as a decimal',
         stem='Mehul adds 3/4, 0.6 and 7/20. What is the total as a decimal?',
         opts=['1.7', '1.07', '1.65', '1.8'],
         hint='Change each fraction into hundredths.',
         sol='3/4 = 0.75 and 7/20 = 0.35. 0.75 + 0.6 + 0.35 = 1.7.'),
    dict(ch='3', scen='3.5 kg rice at ₹48.40 per kg paid with ₹200',
         stem='Ankit buys 3.5 kg of rice at ₹48.40 per kg and pays with a ₹200 note. How much change does he get?',
         opts=['₹30.60', '₹31.40', '₹30.40', '₹40.60'],
         hint='3.5 kg is 3 kg and half a kilogram.',
         sol='3 kg cost 3 × 48.40 = ₹145.20. Half a kg costs ₹24.20. Total ₹169.40. Change: 200 − 169.40 = ₹30.60.'),
    dict(ch='3', scen='2/5 on books 1/4 on snacks · ₹140 left',
         stem='Seema spends 2/5 of her pocket money on books and 1/4 of it on snacks. She has ₹140 left. How much pocket money did she have?',
         opts=['₹400', '₹350', '₹560', '₹200'],
         hint='Write both fractions in twentieths.',
         sol='2/5 + 1/4 = 8/20 + 5/20 = 13/20 is spent, so 7/20 is left. 7/20 is ₹140, so 1/20 is ₹20 and the whole is 20 × 20 = ₹400.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='three angles on a straight line each 20 more than the last',
         stem='Three angles make a straight line. The second is 20° more than the first, and the third is 20° more than the second. What is the largest angle?',
         opts=['80°', '60°', '100°', '70°'],
         hint='Angles on a straight line add up to 180°.',
         sol='Take the first angle away from each: the extras are 0°, 20° and 40°, which is 60°. 180° − 60° = 120°, so each base part is 40°. The angles are 40°, 60° and 80°.'),
    dict(ch='5', scen='triangle with two 7 cm sides and 60 degrees between them',
         stem='A triangle has two sides of 7 cm with an angle of 60° between them. What type of triangle is it?',
         opts=['Equilateral', 'Isosceles but not equilateral', 'Scalene', 'Right-angled'],
         hint='In a triangle with two equal sides, the two other angles are equal.',
         sol='The other two angles are equal and add up to 180° − 60° = 120°, so each is 60°. All three angles are 60°, so all sides are equal: equilateral.'),
    dict(ch='5', scen='which regular polygon cannot tile a floor alone',
         stem='Tiles of only one shape must cover a floor with no gaps or overlaps. Which of these regular shapes can NOT do it?',
         opts=['Regular pentagon', 'Equilateral triangle', 'Square', 'Regular hexagon'],
         hint='At each corner the angles must add up to 360°.',
         sol='Corner angles: triangle 60° (6 make 360°), square 90° (4 make 360°), hexagon 120° (3 make 360°). A regular pentagon has 108° corners; 3 make 324° and 4 make 432°, so they never fit exactly.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='2 cm cubes in a 10 by 8 by 6 cm box',
         stem='How many cubes with 2 cm edges can be packed into a box that is 10 cm long, 8 cm wide and 6 cm high?',
         opts=['60', '480', '120', '40'],
         hint='Count how many cubes fit along each edge.',
         sol='Along the length: 10 ÷ 2 = 5. Width: 4. Height: 3. 5 × 4 × 3 = 60 cubes. (480 is the volume divided by 1, not by 8.)'),
    dict(ch='6', scen='area of an L-shaped plot with a corner removed',
         fig=drawing(170, 135, l_shape()),
         stem='What is the area of this shape? All corners are right angles.',
         opts=['100 cm²', '120 cm²', '80 cm²', '110 cm²'],
         hint='Think of a 12 cm by 10 cm rectangle with a piece missing.',
         sol='The full rectangle is 12 × 10 = 120 cm². The missing corner is 4 cm by 5 cm = 20 cm². 120 − 20 = 100 cm².'),
    dict(ch='6', scen='right triangle with area 54 and one side 9 · perimeter',
         stem='A right-angled triangle has an area of 54 cm². One of the sides that make the right angle is 9 cm. Its longest side is 15 cm. What is its perimeter?',
         opts=['36 cm', '33 cm', '42 cm', '30 cm'],
         hint='Area = half of (one side × the other side) at the right angle.',
         sol='Half of 9 × (other side) = 54, so 9 × (other side) = 108 and the other side is 12 cm. Perimeter: 9 + 12 + 15 = 36 cm.'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='pictograph of apples sold against a 300 kg target',
         fig=drawing(300, 190, pict([('Monday', 3), ('Tuesday', 5), ('Wednesday', 2), ('Thursday', 4)], '🍎', '20 kg')),
         stem='The pictograph shows apples sold by a shop. Its target was 300 kg for the four days. What happened?',
         opts=['It missed by 20 kg', 'It beat it by 20 kg', 'It missed by 1 kg', 'It beat it by 80 kg'],
         hint='Each symbol stands for 20 kg.',
         sol='Symbols: 3 + 5 + 2 + 4 = 14. 14 × 20 = 280 kg. 300 − 280 = 20, so it missed the target by 20 kg.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='walk 6 km at 5 km/h and cycle back at 15 km/h · total time',
         stem='Raghav walks from home to a lake at 5 km/h. The lake is 6 km away. He cycles back at 15 km/h. How long does the whole trip take?',
         opts=['1 h 36 min', '1 h 24 min', '2 h', '1 h 32 min'],
         hint='Find each time in minutes.',
         sol='Walking: 6 km at 5 km/h takes 6/5 h = 72 minutes. Cycling: 6 km at 15 km/h takes 6/15 h = 24 minutes. Total 96 minutes = 1 h 36 min.'),
    dict(ch='9', scen='bus with a 30 minute stop · average speed for whole journey',
         stem='A bus travels 120 km in 3 hours, stops for 30 minutes, then travels 90 km in 1.5 hours. What is its average speed for the whole journey, including the stop?',
         opts=['42 km/h', '52.5 km/h', '40 km/h', '45 km/h'],
         hint='Average speed = total distance ÷ total time.',
         sol='Distance: 120 + 90 = 210 km. Time: 3 + 0.5 + 1.5 = 5 hours. 210 ÷ 5 = 42 km/h. (52.5 forgets the stop: 210 ÷ 4.)'),
    dict(ch='9', scen='seconds in 2.5 hours minus 75 minutes',
         stem='How many seconds are there in 2.5 hours minus 75 minutes?',
         opts=['4,500', '5,400', '4,200', '2,700'],
         hint='Change both to minutes first.',
         sol='2.5 hours = 150 minutes. 150 − 75 = 75 minutes. 75 × 60 = 4,500 seconds.'),
    dict(ch='9', scen='12 bananas at ₹4.50 and 2.5 kg apples at ₹160 paid with ₹500',
         stem='Rani buys 12 bananas at ₹4.50 each and 2.5 kg of apples at ₹160 per kg. She pays with a ₹500 note. How much change does she get?',
         opts=['₹46', '₹54', '₹96', '₹36'],
         hint='2.5 kg is 2 kg and half a kg.',
         sol='Bananas: 12 × 4.50 = ₹54. Apples: 2 × 160 + 80 = ₹400. Total ₹454. Change: 500 − 454 = ₹46.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='doubling series from 3 · eighth term',
         fig=cards([3, 6, 12, 24, '…'], size=40),
         stem='Each number in this series is double the one before. What is the 8th number?',
         opts=['384', '192', '768', '48'],
         hint='Keep doubling and count carefully.',
         sol='3, 6, 12, 24, 48, 96, 192, 384. The 8th number is 384.'),
    dict(ch='10', scen='1 January Wednesday in a non-leap year · day of 1 March',
         stem='In a year that is not a leap year, 1 January is a Wednesday. What day of the week is 1 March?',
         opts=['Saturday', 'Friday', 'Sunday', 'Wednesday'],
         hint='Count the days from 1 January to 1 March.',
         sol='January has 31 days and February 28, so 1 March is 59 days after 1 January. 59 = 8 weeks + 3 days. 3 days after Wednesday is Saturday.'),
    dict(ch='10', scen='plus or minus signs between 1 to 7 · impossible result',
         fig=equations([['1 ? 2 ? 3 ? 4 ? 5 ? 6 ? 7']], size=28),
         stem='Tejas puts a + or − sign in place of each question mark. Which of these results can he NEVER get?',
         opts=['9', '2', '0', '14'],
         hint='What is 1 + 2 + … + 7? Does changing a + into a − change odd or even?',
         sol='With all + signs the total is 28, which is even. Changing a + into a − takes away twice that number, which keeps the total even. So an odd result like 9 is impossible. (2: subtract 6 and 7. 0: subtract 2, 5 and 7. 14: subtract 2 and 5.)'),
    dict(ch='10', scen='ways to make ₹50 from ₹5 ₹10 and ₹20',
         stem='Bhavna has many ₹5 coins, ₹10 notes and ₹20 notes. In how many different ways can she make exactly ₹50?',
         opts=['12', '10', '9', '15'],
         hint='Count the ways with no ₹20 note, with one, and with two.',
         sol='No ₹20: make ₹50 from ₹5 and ₹10 with 0 to 5 tens: 6 ways. One ₹20: make ₹30: 4 ways. Two ₹20: make ₹10: 2 ways. 6 + 4 + 2 = 12.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='HCF 6 LCM 36 one number 12 · the other',
         stem='Two numbers have HCF 6 and LCM 36. One of them is 12. What is the other number?',
         opts=['18', '24', '36', '30'],
         hint='The other number is a multiple of 6 and a factor of 36. Test them.',
         sol='The other number must be a multiple of 6 that divides 36: 6, 12, 18 or 36. With 12: 6 gives LCM 12; 12 gives HCF 12; 36 gives HCF 12. Only 18 works: HCF(12, 18) = 6 and LCM(12, 18) = 36.'),
    dict(ch='3+10', scen='fractions 1/2 2/3 3/4 · first greater than 0.9',
         fig=cards(['1/2', '2/3', '3/4', '4/5', '…'], size=40),
         stem='The pattern continues in the same way. Which is the first fraction in the pattern that is greater than 0.9?',
         opts=['10/11', '9/10', '11/12', '8/9'],
         hint='Each fraction is 1 minus a unit fraction: 1/2 = 1 − 1/2, 2/3 = 1 − 1/3, …',
         sol='The fractions are 1 − 1/2, 1 − 1/3, 1 − 1/4, … To be more than 0.9, the part taken away must be less than 1/10. 9/10 = 0.9 exactly, not more. The next, 10/11 = 1 − 1/11, is the first one greater than 0.9.'),
    dict(ch='6+10', scen='staircase of cubes with 8 steps · cubes needed',
         stem='Lavanya builds a staircase from 1 cm cubes. The 1st step is 1 cube high, the 2nd is 2 cubes high, and so on. Each step is 1 cube wide and 1 cube deep. What is the volume of a staircase with 8 steps?',
         opts=['36 cm³', '28 cm³', '45 cm³', '64 cm³'],
         hint='Add 1 + 2 + 3 + … + 8.',
         sol='Cubes: 1 + 2 + … + 8. Pair 1 with 8, 2 with 7, 3 with 6, 4 with 5: 4 pairs of 9 = 36. Each cube is 1 cm³, so 36 cm³.'),
    dict(ch='1+9', scen='building dated MCMXCVIII · age in 2026',
         stem='A school building has MCMXCVIII carved above its door, the year it was built. How many years old is the building in 2026?',
         opts=['28', '38', '32', '18'],
         hint='MCM is 1900.',
         sol='MCMXCVIII = 1000 + 900 + 90 + 8 = 1998. 2026 − 1998 = 28 years.'),
    dict(ch='3+9', scen='cyclist 0.75 km every 3 minutes · distance in 1 h 12 min',
         stem='A cyclist covers 0.75 km every 3 minutes. How far does she go in 1 hour 12 minutes at the same speed?',
         opts=['18 km', '24 km', '16.5 km', '21.6 km'],
         hint='How many 3-minute blocks are in 1 hour 12 minutes?',
         sol='1 h 12 min = 72 minutes = 24 blocks of 3 minutes. 24 × 0.75 = 18 km.'),
]
