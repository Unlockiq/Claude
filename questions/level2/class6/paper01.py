# AMO Level-2 · Class 6 · Practice Paper 1
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


def l_garden():
    s = 12
    P = lambda x, y: (10 + x * s, 10 + y * s)
    return [('poly', [P(0, 0), P(7, 0), P(7, 3), P(12, 3), P(12, 8), P(0, 8)], 'green'),
            ('text', *P(6, 9), '12 cm', 11), ('text', *P(-1.7, 4), '8 cm', 11), ('text', *P(3.5, -0.8), '7 cm', 11),
            ('text', *P(10, 2.4), '5 cm', 11), ('text', *P(8.4, 0.9), '3 cm', 11)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='three consecutive numbers with product 2,730',
         stem='Three consecutive whole numbers multiply to give 2,730. What is the largest of the three numbers?',
         opts=['15', '14', '13', '16'],
         hint='Write 2,730 as a product of primes and regroup the primes.',
         sol='2,730 = 2 × 3 × 5 × 7 × 13. Regroup: 13 × (2 × 7) × (3 × 5) = 13 × 14 × 15. The largest is 15.'),
    dict(ch='1', scen='Leh temperature rising then falling through the day',
         stem='At 6 AM the temperature in Leh was −8°C. It rose by 3°C every hour until noon, then fell by 2°C every hour until 5 PM. What was the temperature at 5 PM?',
         opts=['0°C', '2°C', '−2°C', '10°C'],
         hint='Count the hours of rising and the hours of falling separately.',
         sol='6 AM to noon is 6 hours: −8 + 6 × 3 = −8 + 18 = 10°C. Noon to 5 PM is 5 hours: 10 − 5 × 2 = 0°C.'),
    dict(ch='1', scen='three bells every 12 15 and 20 minutes from 8 AM to 6 PM',
         stem='Three temple bells ring every 12, 15 and 20 minutes. They ring together at 8:00 AM. How many times do they ring together from 8:00 AM to 6:00 PM, counting both?',
         opts=['11', '10', '12', '6'],
         hint='Find the LCM of 12, 15 and 20.',
         sol='LCM of 12, 15 and 20 is 60 minutes, so they ring together every hour: 8, 9, …, 18 o\'clock. That is 11 times.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='120 minus nested brackets with 48 over 16 minus 3 times 4',
         stem='What is the value of 120 − [48 ÷ {16 − (3 × 4)} + 5 × 6]?',
         opts=['78', '62', '138', '90'],
         hint='Work from the innermost bracket outwards.',
         sol='(3 × 4) = 12. {16 − 12} = 4. 48 ÷ 4 = 12. 12 + 5 × 6 = 12 + 30 = 42. 120 − 42 = 78.'),
    dict(ch='2', scen='sum of all integers from −25 to 30',
         stem='What is the sum of all the integers from −25 to 30, including both?',
         opts=['140', '30', '155', '0'],
         hint='Pair each negative integer with its positive partner.',
         sol='−25 + 25 = 0, −24 + 24 = 0, …, and 0 adds nothing. The integers from −25 to 25 add up to 0. What is left is 26 + 27 + 28 + 29 + 30 = 140.'),
    dict(ch='2', scen='98 times 47 plus 2 times 47 against 125 times 37 times 8',
         stem='Arun works out 98 × 47 + 2 × 47. Jaya works out 125 × 37 × 8. Both use number properties instead of long multiplication. How much larger is Jaya\'s answer?',
         opts=['32,300', '4,700', '37,000', '31,300'],
         hint='Use the distributive property for Arun and regroup 125 × 8 for Jaya.',
         sol='Arun: 47 × (98 + 2) = 47 × 100 = 4,700. Jaya: (125 × 8) × 37 = 1,000 × 37 = 37,000. Difference: 37,000 − 4,700 = 32,300.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='second smallest of 3/8 0.36 37% and 7/20',
         stem='Which is the 2nd smallest of these: 3/8, 0.36, 37%, 7/20?',
         opts=['0.36', '7/20', '37%', '3/8'],
         hint='Change all four into decimals.',
         sol='3/8 = 0.375, 0.36, 37% = 0.37 and 7/20 = 0.35. In order: 0.35, 0.36, 0.37, 0.375. The 2nd smallest is 0.36.'),
    dict(ch='3', scen='school of 1,250 with 48% girls · spectacle wearers',
         stem='A school has 1,250 students and 48% of them are girls. 25% of the girls and 20% of the boys wear spectacles. How many students wear spectacles?',
         opts=['280', '281', '250', '300'],
         hint='Find the number of girls and boys first.',
         sol='Girls: 48% of 1,250 = 600, so boys = 650. Girls with spectacles: 25% of 600 = 150. Boys: 20% of 650 = 130. Total 150 + 130 = 280.'),
    dict(ch='3', scen='price raised 25% then cut 20%',
         stem='A bicycle costs ₹800. Its price is raised by 25%. Later the new price is reduced by 20%. What is the final price?',
         opts=['₹800', '₹840', '₹760', '₹820'],
         hint='The 20% is taken from the new, higher price.',
         sol='After the rise: 800 + 25% of 800 = 800 + 200 = ₹1,000. After the cut: 1,000 − 20% of 1,000 = 1,000 − 200 = ₹800. (₹840 wrongly takes the net change as +5%.)'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='matchstick squares in a row · sticks for 25 squares',
         stem='Squares are made in a row with matchsticks: 1 square uses 4 sticks, 2 squares use 7, 3 squares use 10. How many sticks do 25 squares use?',
         opts=['76', '100', '75', '79'],
         hint='Each new square adds 3 sticks. Write an expression for n squares.',
         sol='The first square uses 4 sticks and each new square adds 3, so n squares use 3n + 1 sticks. For n = 25: 3 × 25 + 1 = 76.'),
    dict(ch='4', scen='ab minus bc plus ca with a −2 b 3 c −4',
         stem='If a = −2, b = 3 and c = −4, what is the value of ab − bc + ca?',
         opts=['14', '−10', '2', '−14'],
         hint='Work out each product carefully with its sign.',
         sol='ab = −2 × 3 = −6. bc = 3 × (−4) = −12. ca = −4 × (−2) = 8. ab − bc + ca = −6 − (−12) + 8 = −6 + 12 + 8 = 14.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='reflex angle between clock hands at 7 o\'clock',
         stem='At exactly 7 o\'clock, the hands of a clock make two angles. What is the size of the reflex angle?',
         opts=['210°', '150°', '230°', '240°'],
         hint='Each hour mark is 30° apart. The reflex angle is more than 180°.',
         sol='At 7 o\'clock the hands are 5 hour-marks apart the short way: 5 × 30° = 150°. The reflex angle is the other way round: 360° − 150° = 210°.'),
    dict(ch='5', scen='triangle with angles x 2x and x plus 20 · type and largest',
         stem='In a triangle, one angle is twice the smallest angle and the third angle is 20° more than the smallest. What type of triangle is it, and what is its largest angle?',
         opts=['Acute, 80°', 'Obtuse, 100°', 'Right, 90°', 'Acute, 60°'],
         hint='The three angles add up to 180°.',
         sol='Smallest + 2 × smallest + (smallest + 20°) = 180°, so 4 × smallest = 160° and the smallest is 40°. The angles are 40°, 80° and 60°. All are less than 90°, so it is acute, and the largest is 80°.'),
    dict(ch='5', scen='diagonals of a regular octagon',
         stem='How many diagonals does a regular octagon have?',
         opts=['20', '16', '28', '40'],
         hint='From each corner, you cannot draw a diagonal to itself or to its two neighbours.',
         sol='From each of the 8 corners there are 8 − 3 = 5 diagonals. 8 × 5 = 40 counts every diagonal twice (once from each end). So there are 40 ÷ 2 = 20.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='L-shaped card 12 by 8 with 5 by 3 corner cut · perimeter and area',
         fig=drawing(170, 120, l_garden()),
         stem='A 12 cm by 8 cm card has a 5 cm by 3 cm rectangle cut from one corner, as shown. What are the perimeter and the area of the card that is left?',
         opts=['40 cm, 81 cm²', '34 cm, 81 cm²', '40 cm, 96 cm²', '46 cm, 81 cm²'],
         hint='Cutting a corner rectangle does not change the perimeter. Why?',
         sol='The two new edges (5 cm and 3 cm) replace the two edges that were cut away, so the perimeter stays 2 × (12 + 8) = 40 cm. Area: 12 × 8 − 5 × 3 = 96 − 15 = 81 cm².'),
    dict(ch='6', scen='open box 20 by 15 by 10 · paper to cover outside',
         stem='A box with no lid is 20 cm long, 15 cm wide and 10 cm high. How much paper is needed to cover its outside exactly?',
         opts=['1,000 cm²', '1,300 cm²', '700 cm²', '3,000 cm²'],
         hint='There are only 5 faces to cover.',
         sol='Base: 20 × 15 = 300 cm². Two long sides: 2 × 20 × 10 = 400 cm². Two short sides: 2 × 15 × 10 = 300 cm². Total 300 + 400 + 300 = 1,000 cm². (1,300 includes the lid.)'),
    dict(ch='6', scen='4 cm cubes packed into a 20 by 12 by 10 box',
         stem='How many cubes of edge 4 cm can be packed into a box 20 cm long, 12 cm wide and 10 cm high?',
         opts=['30', '37', '40', '36'],
         hint='Count how many cubes fit along each edge. Parts of a cube do not count.',
         sol='Along 20 cm: 5 cubes. Along 12 cm: 3 cubes. Along 10 cm: only 2 cubes (2 cm is wasted). 5 × 3 × 2 = 30. (Dividing volumes, 2,400 ÷ 64 = 37.5, ignores the wasted space.)'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='bar graph of books read · top two minus bottom two',
         fig=drawing(330, 210, bars([('Asha', 12), ('Dev', 18), ('Gita', 9), ('Hari', 15), ('Isha', 21)], 24, 3, 'Books read in May'), scale=1.0),
         stem='The bar graph shows the books read by five friends. How many more books did the top two readers read than the bottom two readers together?',
         opts=['18', '12', '21', '15'],
         hint='Read each bar against the gridlines.',
         sol='Top two: Isha 21 + Dev 18 = 39. Bottom two: Gita 9 + Asha 12 = 21. 39 − 21 = 18.'),
    dict(ch='8', scen='frequency table of quiz marks · percent scoring at least 8',
         fig=table(['Marks', '5', '6', '7', '8', '9'], [['Students', '2', '4', '7', '5', '2']], widths=[90, 50, 50, 50, 50, 50]),
         stem='The table shows the marks of a class in a quiz. What percentage of the class scored at least 8 marks?',
         opts=['35%', '25%', '45%', '70%'],
         hint='Find the total number of students first.',
         sol='Total: 2 + 4 + 7 + 5 + 2 = 20 students. At least 8 marks: 5 + 2 = 7 students. 7 out of 20 = 35/100 = 35%.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='300 m train crossing a 700 m bridge at 72 km/h',
         stem='A train 300 m long runs at 72 km/h. How long does it take to cross a bridge 700 m long completely?',
         opts=['50 s', '35 s', '15 s', '14 s'],
         hint='The train must cover the bridge plus its own length. 72 km/h = 20 m every second.',
         sol='Distance = 700 + 300 = 1,000 m. 72 km/h = 72,000 m in 3,600 s = 20 m/s. Time = 1,000 ÷ 20 = 50 s. (35 s forgets the train\'s length.)'),
    dict(ch='9', scen='₹4,500 shared 2:3:4 then half of the largest share given away',
         stem='Asha, Bina and Chetan share ₹4,500 in the ratio 2 : 3 : 4. Chetan then gives half of his share to Asha. How much does Asha have now?',
         opts=['₹2,000', '₹1,000', '₹1,500', '₹2,500'],
         hint='There are 2 + 3 + 4 = 9 equal parts.',
         sol='One part = 4,500 ÷ 9 = ₹500. Asha ₹1,000, Bina ₹1,500, Chetan ₹2,000. Half of Chetan\'s share is ₹1,000, so Asha has 1,000 + 1,000 = ₹2,000.'),
    dict(ch='9', scen='12 workers on a 10-day wall joined by 6 more after 4 days',
         stem='12 workers can build a wall in 10 days. They work for 4 days, and then 6 more workers join them at the same rate. How many days does the whole wall take?',
         opts=['8', '10', '6', '9'],
         hint='Count the work in worker-days.',
         sol='The wall needs 12 × 10 = 120 worker-days. In 4 days, 12 workers do 48 worker-days, leaving 72. Now 18 workers work: 72 ÷ 18 = 4 more days. Total 4 + 4 = 8 days.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='Monday 9 AM plus 100 hours',
         stem='It is 9 AM on a Monday. What day and time will it be exactly 100 hours later?',
         opts=['Friday, 1 PM', 'Thursday, 1 PM', 'Friday, 11 AM', 'Saturday, 1 PM'],
         hint='100 hours = some whole days and some hours.',
         sol='100 = 4 × 24 + 4, so 100 hours is 4 days and 4 hours. 4 days after Monday 9 AM is Friday 9 AM. 4 hours later is Friday, 1 PM.'),
    dict(ch='10', scen='which number could be the sum of seven odd numbers',
         stem='Kavya adds seven odd numbers. Which of these could be her total?',
         opts=['45', '50', '64', '38'],
         hint='Odd + odd is even. What happens with seven odd numbers?',
         sol='Pairs of odd numbers add to even numbers. Seven odd numbers make three pairs and one extra odd number, so the total is even + odd = odd. Only 45 is odd. (For example 1 + 3 + 5 + 7 + 9 + 11 + 9 = 45.)'),
    dict(ch='10', scen='spending half plus ₹10 at two shops with ₹20 left',
         stem='Tara spent half her money and ₹10 more at one shop. At a second shop she spent half of what was left and ₹10 more. She had ₹20 left. How much did she start with?',
         opts=['₹140', '₹120', '₹100', '₹160'],
         hint='Work backwards from ₹20, undoing each step.',
         sol='Before the last ₹10 she had 20 + 10 = ₹30, which was half, so she had ₹60 after the first shop. Before the first ₹10: 60 + 10 = ₹70, which was half, so she started with ₹140.'),

    # ---------------- Mixed Problems
    dict(ch='4+10', scen='dot pattern 5 9 13 · figure with 101 dots',
         fig=cards([5, 9, 13, '…'], size=40),
         stem='In a number pattern the 1st term is 5, the 2nd is 9 and the 3rd is 13. Which term is exactly 101?',
         opts=['25th', '24th', '26th', '20th'],
         hint='Write the nth term as an expression, then work backwards from 101.',
         sol='Each term adds 4, so the nth term is 4n + 1. Taking away the 1 from 101 leaves 100, and 100 = 4 × 25. So 101 is the 25th term.'),
    dict(ch='1+10', scen='numbers 1 to 1,000 divisible by 6 but not by 9',
         stem='How many numbers from 1 to 1,000 are divisible by 6 but not by 9?',
         opts=['111', '166', '110', '55'],
         hint='A number divisible by both 6 and 9 is divisible by their LCM.',
         sol='Multiples of 6 up to 1,000: 1,000 ÷ 6 = 166 (remainder 4). Multiples of both 6 and 9 are multiples of 18: 1,000 ÷ 18 = 55 (remainder 10). 166 − 55 = 111.'),
    dict(ch='3+9', scen='two 1,000 L tanks · 20% then 50 L against 50 L then 20%',
         stem='Two tanks each hold 1,000 L of water. From Tank A, 20% of the water is used and then 50 L more. From Tank B, 50 L is used and then 20% of what is left. Which tank has more water left, and by how much?',
         opts=['Tank B, by 10 L', 'Tank A, by 10 L', 'Both have the same', 'Tank B, by 40 L'],
         hint='Work out what is left in each tank, one step at a time.',
         sol='Tank A: 1,000 − 200 = 800 L, then 800 − 50 = 750 L. Tank B: 1,000 − 50 = 950 L, then 950 − 20% of 950 = 950 − 190 = 760 L. Tank B has 10 L more.'),
    dict(ch='5+6', scen='rectangle cut by a line from a corner to the middle of the far long side',
         stem='A rectangle is 12 cm long and 8 cm wide. A straight cut goes from one corner to the middle of the opposite long side, cutting off a right-angled triangle. What is the area of the larger piece?',
         opts=['72 cm²', '48 cm²', '84 cm²', '24 cm²'],
         hint='The triangle has the 8 cm side and half of the 12 cm side as its two shorter sides.',
         sol='The triangle\'s shorter sides are 8 cm and 6 cm, so its area is 8 × 6 ÷ 2 = 24 cm². The rectangle is 96 cm². The larger piece (a four-sided shape) is 96 − 24 = 72 cm².'),
    dict(ch='4+9', scen='cab fare ₹50 plus ₹12 per km · distance for ₹386',
         stem='A cab charges ₹50 to start plus ₹12 for every km. Riya pays ₹386 for her ride. How many km did she travel?',
         opts=['28', '32', '27', '23'],
         hint='Write the fare for n km, then work backwards.',
         sol='Fare = 50 + 12n. 386 − 50 = 336 is the distance part. 336 ÷ 12 = 28 km.'),
]
