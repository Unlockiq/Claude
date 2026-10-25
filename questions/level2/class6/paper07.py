# AMO Level-2 · Class 6 · Practice Paper 7


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


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='4,56,78,912 rounded to nearest lakh and nearest crore · difference',
         stem='Kriti rounds 4,56,78,912 to the nearest lakh and also to the nearest crore. What is the difference between her two answers?',
         opts=['43,00,000', '44,00,000', '3,00,000', '43,21,088'],
         hint='Look at the digits just after the lakhs place and just after the crores place.',
         sol='Nearest lakh: the thousands part 78,912 is more than 50,000, so round up to 4,57,00,000. Nearest crore: 56 lakh is more than 50 lakh, so round up to 5,00,00,000. Difference: 43,00,000.'),
    dict(ch='1', scen='factors of 48 and how many are even',
         stem='How many factors does 48 have, and how many of them are even?',
         opts=['10 factors, 8 even', '10 factors, 5 even', '8 factors, 6 even', '12 factors, 8 even'],
         hint='List the factors in pairs: 1 × 48, 2 × 24, …',
         sol='Factor pairs: 1 × 48, 2 × 24, 3 × 16, 4 × 12, 6 × 8. That is 10 factors. Only 1 and 3 are odd, so 8 are even.'),
    dict(ch='1', scen='product of the non-zero integers from −5 to 5',
         stem='What is the product of all the integers from −5 to 5, leaving out 0?',
         opts=['−14,400', '14,400', '0', '−120'],
         hint='There are five negative numbers in the product.',
         sol='(−1)(−2)(−3)(−4)(−5) = −120, since five negatives give a negative. 1 × 2 × 3 × 4 × 5 = 120. Product = −120 × 120 = −14,400.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='which bracketing of 12 minus 4 times 2 plus 6 over 3 gives −4',
         stem='Which of these has the value −4?',
         opts=['12 − 4 × (2 + 6 ÷ 3)', '(12 − 4) × 2 + 6 ÷ 3', '12 − 4 × 2 + 6 ÷ 3', '12 − (4 × 2 + 6) ÷ 2'],
         hint='Work out each one, brackets first, then × and ÷, then + and −.',
         sol='12 − 4 × (2 + 2) = 12 − 16 = −4. ✓ (12 − 4) × 2 + 2 = 18. 12 − 8 + 2 = 6. 12 − 14 ÷ 2 = 5.'),
    dict(ch='2', scen='−3 times bracket minus quotient of negatives times −1',
         stem='What is the value of (−3) × [(−2) + 5] − [(−12) ÷ (−4)] × (−1)?',
         opts=['−6', '−12', '6', '0'],
         hint='Work out both square brackets first.',
         sol='(−2) + 5 = 3 and (−12) ÷ (−4) = 3. So the expression is (−3) × 3 − 3 × (−1) = −9 + 3 = −6.'),
    dict(ch='2', scen='4 times 17 times 25 minus 17 times 99',
         stem='Use number properties to find (4 × 17 × 25) − (17 × 99).',
         opts=['17', '1', '117', '−17'],
         hint='4 × 25 = 100.',
         sol='4 × 17 × 25 = 17 × 100. Then 17 × 100 − 17 × 99 = 17 × (100 − 99) = 17.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='how many of five numbers exceed one third',
         stem='How many of these are greater than 1/3: 0.33, 34%, 2/7, 0.334, 5/16?',
         opts=['2', '3', '1', '4'],
         hint='1/3 = 0.3333… Change each number into a decimal.',
         sol='0.33 < 0.333…; 34% = 0.34 > 0.333…; 2/7 = 0.2857…; 0.334 > 0.3333…; 5/16 = 0.3125. Only 34% and 0.334: 2 numbers.'),
    dict(ch='3', scen='20 kg melon 90% water dried to 80% water',
         stem='A 20 kg watermelon is 90% water. After lying in the sun, it is 80% water. What does it weigh now?',
         opts=['10 kg', '18 kg', '16 kg', '12 kg'],
         hint='Only the water dries. The non-water part stays the same.',
         sol='Non-water part: 10% of 20 kg = 2 kg. Afterwards this 2 kg is 20% of the melon, so the melon weighs 2 × 5 = 10 kg.'),
    dict(ch='3', scen='120 runs with 40% in fours and 15% in sixes · boundaries',
         stem='A batter scores 120 runs. 40% of the runs come from fours and 15% from sixes. How many boundaries (fours and sixes) does she hit?',
         opts=['15', '66', '12', '18'],
         hint='Find the runs from fours and from sixes first.',
         sol='Runs from fours: 40% of 120 = 48, which is 12 fours. Runs from sixes: 15% of 120 = 18, which is 3 sixes. Boundaries: 12 + 3 = 15.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='simplify 3x plus 2y minus x minus 4y plus 2 times x minus y',
         stem='Simplify (3x + 2y) − (x − 4y) + 2(x − y).',
         opts=['4x + 4y', '4x − 4y', '2x + 4y', '4x + 2y'],
         hint='The minus sign in front of (x − 4y) changes both signs inside.',
         sol='3x + 2y − x + 4y + 2x − 2y = (3x − x + 2x) + (2y + 4y − 2y) = 4x + 4y.'),
    dict(ch='4', scen='3 shirts and 2 trousers with ₹100 off · s 450 t 800',
         stem='Shirts cost ₹s each and trousers ₹t each. Raghav buys 3 shirts and 2 trousers and gets ₹100 off the bill. Write his bill and find it when s = 450 and t = 800.',
         opts=['3s + 2t − 100; ₹2,850', '3s + 2t − 100; ₹2,950', '5(s + t) − 100; ₹6,150', '3s + 2t + 100; ₹3,050'],
         hint='Add the costs, then take off ₹100.',
         sol='Bill = 3s + 2t − 100. At s = 450, t = 800: 1,350 + 1,600 − 100 = ₹2,850.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='angles a 2a 3a on a straight line · largest and type',
         stem='Three angles on a straight line are a, 2a and 3a. What is the largest of them, and what type of angle is it?',
         opts=['90°, right', '60°, acute', '120°, obtuse', '90°, straight'],
         hint='Angles on a straight line add up to 180°.',
         sol='a + 2a + 3a = 6a = 180°, so a = 30°. The largest is 3a = 90°, a right angle.'),
    dict(ch='5', scen='smallest number of acute angles in any triangle',
         stem='Every triangle has at least how many acute angles?',
         opts=['2', '1', '3', '0'],
         hint='Could a triangle have two angles of 90° or more?',
         sol='Two angles of 90° or more would already add to 180° or more, leaving nothing for the third angle. So at most one angle is 90° or more, and at least 2 angles are acute.'),
    dict(ch='5', scen='polygon with as many diagonals as sides',
         stem='Which polygon has exactly as many diagonals as sides?',
         opts=['Pentagon', 'Hexagon', 'Square', 'Heptagon'],
         hint='Count diagonals with n × (n − 3) ÷ 2.',
         sol='Pentagon: 5 × 2 ÷ 2 = 5 diagonals and 5 sides. ✓ Square: 2 diagonals. Hexagon: 9. Heptagon: 14.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='rectangle with perimeter 46 and area 120 · length',
         stem='A rectangle has perimeter 46 cm and area 120 cm². What is its length (the longer side)?',
         opts=['15 cm', '12 cm', '20 cm', '23 cm'],
         hint='Length + breadth = 23. Which two numbers add to 23 and multiply to 120?',
         sol='Length + breadth = 46 ÷ 2 = 23 and length × breadth = 120. 15 + 8 = 23 and 15 × 8 = 120, so the length is 15 cm.'),
    dict(ch='6', scen='painting a 30 by 20 by 10 box at ₹2 per 100 cm²',
         stem='The outside of a closed box 30 cm × 20 cm × 10 cm is painted. Paint costs ₹2 for every 100 cm². What is the cost?',
         opts=['₹44', '₹120', '₹22', '₹88'],
         hint='Find the total surface area first.',
         sol='Surface area = 2 × (30 × 20 + 30 × 10 + 20 × 10) = 2 × (600 + 300 + 200) = 2,200 cm². Cost = 22 × ₹2 = ₹44.'),
    dict(ch='6', scen='1 cm cubes in a 6 by 5 by 4 cuboid not on the surface',
         stem='A cuboid 6 cm × 5 cm × 4 cm is built from 1 cm cubes. How many of the cubes are completely hidden inside (not on any face)?',
         opts=['24', '60', '96', '120'],
         hint='Remove one layer from every face.',
         sol='Taking one layer off every face leaves an inner block of (6 − 2) × (5 − 2) × (4 − 2) = 4 × 3 × 2 = 24 cubes.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='ice cream sales bar graph · share of the two lowest days',
         fig=drawing(330, 210, bars([('Mon', 24), ('Tue', 36), ('Wed', 18), ('Thu', 42), ('Fri', 30)], 48, 6, 'Ice creams sold')),
         stem='The bar graph shows ice creams sold at a stall. What fraction of the week\'s sales came from the two days with the lowest sales?',
         opts=['7/25', '2/5', '1/5', '3/10'],
         hint='Find the total first, then the two smallest bars.',
         sol='Total: 24 + 36 + 18 + 42 + 30 = 150. Two lowest: Wed 18 + Mon 24 = 42. 42/150 = 7/25.'),
    dict(ch='8', scen='pets owned by 25 children table · total pets and children with at least 2',
         fig=table(['Pets owned', '0', '1', '2', '3', '4'], [['Children', '5', '9', '6', '4', '1']], widths=[110, 50, 50, 50, 50, 50]),
         stem='The table shows how many pets each of 25 children owns. How many pets are there in all, and how many children own at least 2 pets?',
         opts=['37 pets; 11 children', '37 pets; 6 children', '25 pets; 11 children', '40 pets; 11 children'],
         hint='Multiply each number of pets by its number of children.',
         sol='Pets: 0 + 9 + 12 + 12 + 4 = 37. At least 2 pets: 6 + 4 + 1 = 11 children.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='cyclist at 13 m/s lapping a runner at 5 m/s on a 400 m track',
         stem='A runner (5 m/s) and a cyclist (13 m/s) start together from the same point on a 400 m circular track, going the same way. After how long does the cyclist first pass the runner?',
         opts=['50 s', '22 s', '80 s', '31 s'],
         hint='The cyclist must gain one full lap of 400 m.',
         sol='The cyclist gains 13 − 5 = 8 m every second. To gain 400 m takes 400 ÷ 8 = 50 s.'),
    dict(ch='9', scen='60 L milk and water 3:1 changed to 3:2 by adding water',
         stem='A 60-litre mixture has milk and water in the ratio 3 : 1. How much water must be added to make the ratio 3 : 2?',
         opts=['15 L', '20 L', '10 L', '30 L'],
         hint='The milk stays the same.',
         sol='Milk = 45 L and water = 15 L. For 3 : 2, water must be 2/3 of the milk = 30 L. Add 30 − 15 = 15 L.'),
    dict(ch='9', scen='6 machines make 720 bottles in 4 hours · 9 machines in 5 hours',
         stem='6 machines make 720 bottles in 4 hours. How many bottles do 9 such machines make in 5 hours?',
         opts=['1,350', '1,080', '900', '1,620'],
         hint='Find the bottles one machine makes in one hour.',
         sol='One machine makes 720 ÷ (6 × 4) = 30 bottles an hour. 9 machines for 5 hours: 9 × 5 × 30 = 1,350.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='clock losing 10 minutes an hour set at 6 AM shows 6 PM',
         stem='A clock loses 10 minutes every hour. It is set right at 6 AM. Later it shows 6 PM. What is the real time?',
         opts=['8:24 PM', '8:00 PM', '4:00 PM', '7:12 PM'],
         hint='In each real hour, the clock moves only 50 minutes.',
         sol='The clock has moved 12 hours = 720 minutes. It moves 50 minutes per real hour, so 720 ÷ 50 = 14.4 real hours = 14 h 24 min. 6 AM + 14 h 24 min = 8:24 PM.'),
    dict(ch='10', scen='knight returning to its start square in exactly 7 moves',
         stem='Can a chess knight return to its starting square in exactly 7 moves?',
         opts=['No, each move changes the colour of its square', 'Yes, from any square', 'Yes, but only from a corner', 'No, it always needs at least 8 moves'],
         hint='What colour is the square after 1 move, 2 moves, …?',
         sol='Every knight move goes to a square of the other colour. After an odd number of moves, like 7, it is on the opposite colour, so it cannot be back on its start square. (It can return in 2, 4, … moves, so the last option is false.)'),
    dict(ch='10', scen='tank halving then plus 10 L each hour · 30 L after 3 hours',
         stem='Each hour, half the water in a tank leaks out and then 10 litres are poured in. After 3 hours the tank has 30 litres. How much did it have at the start?',
         opts=['100 L', '80 L', '120 L', '60 L'],
         hint='Undo each hour: take away 10, then double.',
         sol='Hour 3: (30 − 10) × 2 = 40. Hour 2: (40 − 10) × 2 = 60. Hour 1: (60 − 10) × 2 = 100 L.'),

    # ---------------- Mixed Problems
    dict(ch='4+10', scen='sequence starting 2 with next equal to 3 times minus 2 · sixth term',
         fig=cards([2, 4, 10, 28, '…'], size=40),
         stem='In this sequence, each number is 3 × (the number before) − 2. What is the 6th number?',
         opts=['244', '82', '226', '246'],
         hint='Keep applying the rule: next = 3 × now − 2.',
         sol='2, 4, 10, 28, then 3 × 28 − 2 = 82, then 3 × 82 − 2 = 244. The 6th number is 244.'),
    dict(ch='1+10', scen='integers between −30 and 30 divisible by neither 2 nor 3',
         stem='How many integers lie strictly between −30 and 30 that are divisible by neither 2 nor 3?',
         opts=['20', '21', '19', '40'],
         hint='Count the positive ones from 1 to 29 and double; 0 is divisible by 2.',
         sol='From 1 to 29: the numbers not divisible by 2 or 3 are 1, 5, 7, 11, 13, 17, 19, 23, 25, 29, which is 10. The negative ones match them: 10 more. 0 is divisible by 2. Total 20.'),
    dict(ch='3+9', scen='25% discount followed by an extra 10% · overall discount',
         stem='A shop gives a 25% discount and then an extra 10% off the discounted price. What is the overall discount on the original price?',
         opts=['32.5%', '35%', '30%', '33%'],
         hint='Try a price of ₹100.',
         sol='₹100 → 25% off → ₹75 → 10% off → ₹67.50. The total discount is ₹32.50 on ₹100, which is 32.5%. (35% wrongly adds the two discounts.)'),
    dict(ch='5+6', scen='square cut along both diagonals into four 9 cm² triangles · perimeter',
         stem='A square is cut along both its diagonals into 4 triangles. Each triangle has area 9 cm². What is the perimeter of the square?',
         opts=['24 cm', '36 cm', '12 cm', '18 cm'],
         hint='Find the area of the square first.',
         sol='The square\'s area is 4 × 9 = 36 cm², so its side is 6 cm (6 × 6 = 36). Perimeter = 4 × 6 = 24 cm.'),
    dict(ch='4+9', scen='plumber ₹200 plus ₹150 an hour against electrician ₹350 plus ₹100 an hour',
         stem='A plumber charges ₹200 for a visit plus ₹150 an hour. An electrician charges ₹350 for a visit plus ₹100 an hour. For how many hours of work do they charge the same, and how much?',
         opts=['3 hours; ₹650', '3 hours; ₹600', '2 hours; ₹500', '4 hours; ₹750'],
         hint='The electrician starts ₹150 dearer but costs ₹50 less each hour.',
         sol='The difference of ₹150 closes by ₹50 an hour, so after 3 hours they are equal. Plumber: 200 + 450 = ₹650. Electrician: 350 + 300 = ₹650.'),
]
