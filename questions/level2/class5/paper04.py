# AMO Level-2 · Class 5 · Practice Paper 4  (format: see paper01.py)


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


def mid_triangle():
    return [('rect', 10, 10, 160, 100, 'white'), ('poly', [(90, 10), (10, 110), (170, 110)], 'blue'),
            ('text', 90, 0, 'E (middle of the top side)', 10), ('text', 90, 124, '16 cm', 11), ('text', 186, 60, '10 cm', 11)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='smallest number leaving remainder 1 on division by 2 to 6',
         stem='Which is the smallest number greater than 1 that leaves a remainder of 1 when divided by 2, by 3, by 4, by 5 and by 6?',
         opts=['61', '31', '121', '59'],
         hint='One less than the number is divisible by all of 2, 3, 4, 5 and 6.',
         sol='The number minus 1 must be a common multiple of 2, 3, 4, 5 and 6. Their LCM is 60. So the number is 60 + 1 = 61.'),
    dict(ch='1', scen='Roman numerals from I to C that use the letter L',
         stem='Jayesh writes the Roman numerals from I to C. How many of them use the letter L?',
         opts=['50', '49', '40', '39'],
         hint='L means 50. Which numbers need it?',
         sol='40 to 49 are XL to XLIX: 10 numerals. 50 to 89 all start with L: 40 numerals. 90 to 99 use XC and 100 is C, with no L. 10 + 40 = 50.'),
    dict(ch='1', scen='three consecutive primes multiplying to 1001',
         stem='Three prime numbers that come one after another (like 2, 3, 5) multiply to give 1,001. What is their sum?',
         opts=['31', '29', '35', '23'],
         hint='Try dividing 1,001 by 7.',
         sol='1,001 ÷ 7 = 143 and 143 = 11 × 13. So 1,001 = 7 × 11 × 13, which are consecutive primes. 7 + 11 + 13 = 31.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='curly bracket 48 minus round bracket 12 plus 6 times 3 divided by 6 times 5',
         fig=equations([['{48 − (12 + 6 × 3)} ÷ 6 × 5', '=', '?']], size=28),
         stem='Tanmay works out this expression in the correct order. What is the answer?',
         opts=['15', '0.6', '90', '3'],
         hint='Inside the round bracket, multiply before adding.',
         sol='6 × 3 = 18 and 12 + 18 = 30. 48 − 30 = 18. Then from left to right: 18 ÷ 6 = 3 and 3 × 5 = 15. (0.6 wrongly does 6 × 5 first.)'),
    dict(ch='2', scen='6,48,372 rounded to the nearest thousand and nearest lakh',
         stem='Anjali rounds 6,48,372 to the nearest thousand. Mayank rounds it to the nearest lakh. What is the difference between their answers?',
         opts=['48,000', '52,000', '48,372', '1,48,000'],
         hint='To the nearest lakh, look at the ten-thousands digit.',
         sol='Nearest thousand: 6,48,000. Nearest lakh: 6,00,000, because 48,372 is less than 50,000. Difference: 48,000.'),
    dict(ch='2', scen='37 times 46 plus 37 times a box equals 3,700',
         fig=equations([['37 × 46 + 37 × ?', '=', '3,700']], size=30),
         stem='Which number should replace the question mark?',
         opts=['54', '100', '64', '63'],
         hint='3,700 = 37 × 100.',
         sol='37 × 46 + 37 × ? = 37 × (46 + ?). This must be 37 × 100, so 46 + ? = 100 and ? = 54.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='1,500 library books · 20 percent removed · 300 new · percent new',
         stem='A library had 1,500 books. 20% of them were damaged and removed. Then 300 new books were added. What percentage of the books in the library are now new?',
         opts=['20%', '25%', '30%', '15%'],
         hint='First find how many books are in the library now.',
         sol='20% of 1,500 = 300 removed, leaving 1,200. Adding 300 new books gives 1,500. New books: 300 out of 1,500 = 1/5 = 20%.'),
    dict(ch='3', scen='0.36 times 25 divided by 0.9',
         stem='What is 0.36 × 25 ÷ 0.9?',
         opts=['10', '1', '100', '0.1'],
         hint='0.36 × 25 is the same as 36 × 25 ÷ 100.',
         sol='0.36 × 25 = 9. 9 ÷ 0.9 = 90 ÷ 9 = 10.'),
    dict(ch='3', scen='7/10 and 3/4 of equal pizzas · who ate more',
         stem='Sahil ate 7/10 of a pizza. Isha ate 3/4 of a pizza of the same size. Who ate more, and by how much?',
         opts=['Isha, by 1/20', 'Sahil, by 1/20', 'Isha, by 1/10', 'They ate the same'],
         hint='Write both fractions in twentieths.',
         sol='7/10 = 14/20 and 3/4 = 15/20. Isha ate 15/20 − 14/20 = 1/20 of a pizza more.'),
    dict(ch='3', scen='₹2,400 · save 15 percent and give one eighth to charity',
         stem='Payal gets ₹2,400. She saves 15% of it and gives 1/8 of it to charity. How much does she have left to spend?',
         opts=['₹1,740', '₹1,800', '₹2,040', '₹1,640'],
         hint='15% is 10% + 5%.',
         sol='10% of 2,400 = 240 and 5% = 120, so 15% = ₹360. 1/8 of 2,400 = ₹300. Left: 2,400 − 360 − 300 = ₹1,740.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='isosceles triangle with a 40 degree angle · impossible other angle',
         stem='An isosceles triangle has one angle of 40°. Which of these can NOT be one of its other angles?',
         opts=['80°', '100°', '70°', '40°'],
         hint='The 40° angle could be one of the two equal angles, or the odd one.',
         sol='If 40° is one of the equal angles, the angles are 40°, 40° and 100°. If 40° is the odd angle, the other two share 140°: 70° and 70°. So the other angles can be 40°, 100° or 70°, but never 80°.'),
    dict(ch='5', scen='which turn does not make a regular octagon look the same',
         stem='A regular octagon is turned about its centre. Which of these turns does NOT make it look exactly the same as before?',
         opts=['100°', '90°', '135°', '225°'],
         hint='Its order of rotational symmetry is 8. Find the smallest turn first.',
         sol='A regular octagon looks the same 8 times in a full turn, so every turn that is a multiple of 360° ÷ 8 = 45° works. 90° = 2 × 45°, 135° = 3 × 45° and 225° = 5 × 45°. 100° is not a multiple of 45°.'),
    dict(ch='5', scen='walk north right right left · position from start',
         stem='Kirti walks 5 km North. She turns right and walks 3 km, turns right again and walks 9 km, then turns left and walks 3 km. Where is she now from her starting point?',
         opts=['6 km East, 4 km South', '6 km East, 4 km North', '3 km East, 4 km South', '0 km East, 4 km South'],
         hint='Turning right from North faces East; right again faces South.',
         sol='5 km North, then right: 3 km East. Right again: 9 km South, so she is 4 km south of the start. Left from South faces East: 3 km more East. Total 6 km East, 4 km South.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='3 cm cubes cut from a 6 by 9 by 12 cm block',
         stem='A wooden block is 6 cm by 9 cm by 12 cm. How many cubes with 3 cm edges can be cut from it with nothing left over?',
         opts=['24', '72', '48', '18'],
         hint='Count along each edge.',
         sol='6 ÷ 3 = 2, 9 ÷ 3 = 3, 12 ÷ 3 = 4. 2 × 3 × 4 = 24 cubes. (Check: 648 ÷ 27 = 24.)'),
    dict(ch='6', scen='50 cm square tiles on a 12 m by 8.5 m floor',
         stem='A hall floor is 12 m long and 8.5 m wide. It is covered with square tiles of side 50 cm. How many tiles are needed?',
         opts=['408', '204', '102', '816'],
         hint='How many tiles fit along each side?',
         sol='Along 12 m: 24 tiles. Along 8.5 m: 17 tiles. 24 × 17 = 408 tiles.'),
    dict(ch='6', scen='triangle from the middle of the top side of a 16 by 10 rectangle',
         fig=drawing(190, 125, mid_triangle()),
         stem='E is the middle of the top side of a 16 cm by 10 cm rectangle. E is joined to the two bottom corners. What is the area of the shaded triangle?',
         opts=['80 cm²', '40 cm²', '120 cm²', '60 cm²'],
         hint='The two white parts are right-angled triangles.',
         sol='Rectangle: 16 × 10 = 160 cm². Each white right-angled triangle has sides 8 cm and 10 cm: half of 80 = 40 cm². Shaded: 160 − 40 − 40 = 80 cm².'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='pictograph of bicycles sold by four shops · pair making 110',
         fig=drawing(330, 190, pict([('Shop P', 4), ('Shop Q', 7), ('Shop R', 3), ('Shop S', 5)], '🚲', '10 bicycles')),
         stem='The pictograph shows bicycles sold by four shops in a month. Which two shops together sold exactly 110 bicycles?',
         opts=['P and Q', 'Q and R', 'P and S', 'Q and S'],
         hint='Each symbol stands for 10 bicycles, so 110 needs 11 symbols.',
         sol='P 4, Q 7, R 3, S 5 symbols. 11 symbols: P + Q = 4 + 7. (Q + R = 10, P + S = 9, Q + S = 12.)'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='car at 54 km/h from 7:40 AM to 10:10 AM',
         stem='A car leaves at 7:40 AM and arrives at 10:10 AM. It drives at a steady 54 km/h. How far does it travel?',
         opts=['135 km', '162 km', '126 km', '140 km'],
         hint='Find the time taken first.',
         sol='7:40 to 10:10 is 2 hours 30 minutes = 2.5 hours. 54 × 2.5 = 108 + 27 = 135 km.'),
    dict(ch='9', scen='up a 6 km hill at 3 km/h and down at 6 km/h · average speed',
         stem='Sumit walks 6 km up a hill at 3 km/h and comes back down the same path at 6 km/h. What is his average speed for the whole walk?',
         opts=['4 km/h', '4.5 km/h', '5 km/h', '9 km/h'],
         hint='Average speed is not the average of the two speeds.',
         sol='Up: 6 ÷ 3 = 2 hours. Down: 6 ÷ 6 = 1 hour. Total: 12 km in 3 hours, so 12 ÷ 3 = 4 km/h.'),
    dict(ch='9', scen='race time 1 h 4 min 30 s plus 245 seconds',
         stem='The winner of a race took 1 hour 4 minutes 30 seconds. Raju took 245 seconds longer. What was Raju\'s time?',
         opts=['1 h 8 min 35 s', '1 h 6 min 55 s', '1 h 9 min 15 s', '1 h 8 min 15 s'],
         hint='Change 245 seconds into minutes and seconds.',
         sol='245 s = 4 min 5 s (4 × 60 = 240). 1 h 4 min 30 s + 4 min 5 s = 1 h 8 min 35 s.'),
    dict(ch='9', scen='3 kg sugar at ₹46.50 and 2 L oil at ₹138.75 from ₹500',
         stem='Gauri buys 3 kg of sugar at ₹46.50 per kg and 2 litres of oil at ₹138.75 per litre. She had ₹500. How much money is left?',
         opts=['₹83', '₹93', '₹73', '₹83.50'],
         hint='Work out each item, then add.',
         sol='Sugar: 3 × 46.50 = ₹139.50. Oil: 2 × 138.75 = ₹277.50. Total ₹417.00. Left: 500 − 417 = ₹83.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='each number the sum of the two before · 2 3 5 8',
         fig=cards([2, 3, 5, 8, 13, 21, '?'], size=36),
         stem='Find the rule in this series. Which number comes next?',
         opts=['34', '29', '31', '42'],
         hint='Look at 2 + 3 and 3 + 5.',
         sol='Each number is the sum of the two before it: 2 + 3 = 5, 3 + 5 = 8, 5 + 8 = 13, 8 + 13 = 21. Next: 13 + 21 = 34.'),
    dict(ch='10', scen='born Saturday 29 February 2020 · next 29 February birthday',
         stem='Riya was born on Saturday, 29 February 2020. The next 29 February was in 2024. On which day of the week did it fall?',
         opts=['Thursday', 'Saturday', 'Wednesday', 'Friday'],
         hint='The next 29 February is in 2024. Count the days in between.',
         sol='The next 29 February is in 2024. The four years in between have 365 × 4 = 1,460 days plus 1 extra day for 29 February 2024: 1,461 days. 1,461 = 208 weeks + 5 days. 5 days after Saturday is Thursday.'),
    dict(ch='10', scen='which number can be the sum of five consecutive numbers',
         stem='Kavya adds five numbers that come one after another, like 3, 4, 5, 6, 7. Which of these could be her total?',
         opts=['115', '102', '98', '121'],
         hint='The total is 5 times the middle number.',
         sol='The five numbers are spread evenly around the middle one, so the total is 5 × the middle number: a multiple of 5. Only 115 is a multiple of 5: 21 + 22 + 23 + 24 + 25 = 115.'),
    dict(ch='10', scen='3-digit numbers from 0 2 5 7 divisible by 5',
         stem='Rhea makes 3-digit numbers using three different digits from 0, 2, 5 and 7. How many of her numbers are divisible by 5?',
         opts=['10', '12', '6', '8'],
         hint='The number must end in 0 or 5. The first digit cannot be 0.',
         sol='Ending in 0: the first two digits are chosen from 2, 5, 7: 3 × 2 = 6 numbers. Ending in 5: the first digit is 2 or 7 (not 0), then the middle digit has 2 choices: 2 × 2 = 4. 6 + 4 = 10.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='numbers up to 200 divisible by both 6 and 8',
         stem='How many numbers from 1 to 200 are divisible by both 6 and 8?',
         opts=['8', '4', '33', '25'],
         hint='A number divisible by both is a multiple of their LCM, which is not 48.',
         sol='LCM of 6 and 8 is 24. Multiples of 24 up to 200: 24, 48, 72, 96, 120, 144, 168, 192. That is 8. (Using 48 would give only 4.)'),
    dict(ch='3+10', scen='ball dropped from 12.8 m bouncing to half height',
         stem='A ball is dropped from a height of 12.8 m. Each time it bounces, it rises to half the height it fell from. How high does it rise after the 4th bounce?',
         opts=['0.8 m', '1.6 m', '0.4 m', '3.2 m'],
         hint='Halve the height four times.',
         sol='After the bounces it rises to 6.4 m, 3.2 m, 1.6 m and then 0.8 m.'),
    dict(ch='6+10', scen='row of 2 cm squares with perimeter 84 cm',
         stem='Equal squares of side 2 cm are placed side by side in a row to make a long rectangle. How many squares are needed to make a rectangle with a perimeter of 84 cm?',
         opts=['20', '21', '10', '42'],
         hint='With 1 square the perimeter is 8 cm, with 2 squares 12 cm, with 3 squares 16 cm, …',
         sol='Each new square adds 4 cm to the perimeter (2 cm on top and 2 cm below). The perimeter is 4 × (number of squares) + 4. 84 − 4 = 80, and 80 ÷ 4 = 20 squares. Check: 40 cm by 2 cm has perimeter 84 cm.'),
    dict(ch='1+9', scen='₹1,000 in 32 notes of ₹20 and ₹50',
         stem='A shopkeeper has ₹1,000 in ₹20 and ₹50 notes. There are 32 notes in all. How many ₹50 notes are there?',
         opts=['12', '20', '10', '14'],
         hint='Suppose all 32 notes were ₹20 notes.',
         sol='32 notes of ₹20 make ₹640. The rest, ₹360, comes from changing ₹20 notes into ₹50 notes, each adding ₹30. 360 ÷ 30 = 12 notes of ₹50. Check: 12 × 50 + 20 × 20 = 600 + 400 = 1,000.'),
    dict(ch='3+9', scen='bike 1.5 L per 60 km at ₹102 per litre for 340 km',
         stem='A motorbike uses 1.5 litres of petrol for every 60 km. Petrol costs ₹102 per litre. How much does the petrol cost for a 340 km trip?',
         opts=['₹867', '₹850', '₹918', '₹765'],
         hint='Find the petrol used for 20 km first.',
         sol='60 km uses 1.5 L, so 20 km uses 0.5 L. 340 km is 17 lots of 20 km: 17 × 0.5 = 8.5 L. Cost: 8.5 × 102 = 816 + 51 = ₹867.'),
]
