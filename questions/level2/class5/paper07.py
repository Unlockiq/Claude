# AMO Level-2 · Class 5 · Practice Paper 7  (format: see paper01.py)


def bars(data, top, step, unit='', bw=34, gap=22, h=150):
    """Simple bar graph: data = [(label, value)], y axis from 0 to top with gridlines every step."""
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
    dict(ch='1', scen='primes below 60 that end in 3',
         stem='How many prime numbers less than 60 end in the digit 3?',
         opts=['5', '6', '4', '3'],
         hint='Check 3, 13, 23, 33, 43 and 53.',
         sol='3, 13, 23, 43 and 53 are prime. 33 = 3 × 11 is not. So 5.'),
    dict(ch='1', scen='three runners lapping in 4 6 and 9 minutes · laps by the fastest',
         stem='Three runners go round a track. One takes 4 minutes per lap, one 6 minutes and one 9 minutes. They start together. When they are next all together at the start, how many laps has the fastest runner done?',
         opts=['9', '36', '6', '4'],
         hint='Find the LCM of 4, 6 and 9.',
         sol='LCM of 4, 6 and 9 is 36 minutes. The fastest runner takes 4 minutes per lap: 36 ÷ 4 = 9 laps.'),
    dict(ch='1', scen='largest minus smallest 6-digit number from 0 3 5 7 8 9',
         stem='Navya uses each of the digits 0, 3, 5, 7, 8 and 9 exactly once to make 6-digit numbers. What is the difference between the largest and the smallest number she can make?',
         opts=['6,81,741', '6,81,751', '5,81,741', '6,82,741'],
         hint='The smallest number cannot start with 0.',
         sol='Largest: 9,87,530. Smallest: 3,05,789 (0 goes second). 9,87,530 − 3,05,789 = 6,81,741.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='which bracketing of 4 6 2 4 gives 20',
         stem='Which of these expressions has the value 20?',
         opts=['4 × (6 − 2) + 4', '4 × 6 − 2 + 4', '(4 × 6 − 2) + 4', '4 × (6 − 2 + 4)'],
         hint='Work out each one carefully.',
         sol='4 × (6 − 2) + 4 = 16 + 4 = 20. 4 × 6 − 2 + 4 = 26. (4 × 6 − 2) + 4 = 26. 4 × (6 − 2 + 4) = 4 × 8 = 32.'),
    dict(ch='2', scen='3,987 plus 5,012 plus 2,995 rounded to thousands',
         stem='Harini rounds 3,987, 5,012 and 2,995 to the nearest thousand and adds them. How much more is her answer than the exact total?',
         opts=['6', '4', '14', '16'],
         hint='Look at how much each number changed when it was rounded.',
         sol='Rounded: 4,000 + 5,000 + 3,000 = 12,000. Changes: +13, −12, +5, so the estimate is 6 more. Exact total: 11,994.'),
    dict(ch='2', scen='1,000 minus 999 plus 998 minus 997 down to 2 minus 1',
         stem='What is the value of 1,000 − 999 + 998 − 997 + 996 − 995 + … + 2 − 1?',
         opts=['500', '0', '1,000', '499'],
         hint='Group the numbers in pairs: (1,000 − 999), (998 − 997), …',
         sol='Each pair like (1,000 − 999) equals 1. The numbers 1 to 1,000 make 500 pairs, so the total is 500.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='team with 18 wins of 24 · wins needed in next 6 for 80 percent',
         stem='A cricket team has won 18 of its 24 matches. It will play 6 more. How many of those 6 must it win so that it has won 80% of all its matches?',
         opts=['6', '5', '4', '3'],
         hint='Find 80% of the total number of matches.',
         sol='Total matches: 30. 80% of 30 = 24 wins. It has 18, so it needs 6 more: it must win all 6.'),
    dict(ch='3', scen='fraction equal to 0.35 plus 2/5',
         stem='Which fraction is equal to 0.35 + 2/5?',
         opts=['3/4', '37/100', '7/10', '2/3'],
         hint='Change 2/5 into a decimal.',
         sol='2/5 = 0.4. 0.35 + 0.4 = 0.75 = 3/4. (37/100 wrongly adds 35 and 2.)'),
    dict(ch='3', scen='7 pens and 3 erasers for ₹63.50 · price of an eraser',
         stem='Together, 7 pens and 3 erasers cost ₹63.50. One pen costs ₹7.25. What does one eraser cost?',
         opts=['₹4.25', '₹4.50', '₹12.75', '₹3.75'],
         hint='Find the cost of the 7 pens first.',
         sol='7 pens: 7 × 7.25 = ₹50.75. 3 erasers: 63.50 − 50.75 = ₹12.75. One eraser: 12.75 ÷ 3 = ₹4.25.'),
    dict(ch='3', scen='reading 1/4 then 1/3 of the rest with 60 pages left',
         stem='Rekha reads 1/4 of a book on Monday. On Tuesday she reads 1/3 of the pages that are left. She still has 60 pages to read. How many pages does the book have?',
         opts=['120', '180', '240', '96'],
         hint='After Monday, 3/4 of the book is left.',
         sol='After Monday, 3/4 is left. Tuesday: 1/3 of 3/4 = 1/4 of the book. Left: 1 − 1/4 − 1/4 = 1/2 of the book = 60 pages. The book has 120 pages.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='triangle with 52 degrees and two equal angles',
         stem='A triangle has one angle of 52° and its other two angles are equal. What is each equal angle, and what type of triangle is it by its angles?',
         opts=['64°, acute-angled', '64°, obtuse-angled', '128°, obtuse-angled', '76°, acute-angled'],
         hint='The angles add up to 180°.',
         sol='180° − 52° = 128°, shared equally: 64° each. All angles (52°, 64°, 64°) are less than 90°, so it is acute-angled.'),
    dict(ch='5', scen='how many of four quadrilaterals always have equal diagonals',
         stem='How many of these shapes ALWAYS have diagonals of equal length: square, rectangle, rhombus, parallelogram?',
         opts=['2', '1', '3', '4'],
         hint='Think of a tall thin rhombus.',
         sol='The square and the rectangle always have equal diagonals. A rhombus and a parallelogram that are not rectangles have one long and one short diagonal. So 2.'),
    dict(ch='5', scen='facing west then right right left right',
         stem='Kunwar faces West. He turns right, then right again, then left, then right. Which direction does he face now?',
         opts=['East', 'North', 'West', 'South'],
         hint='Turning right from West faces North.',
         sol='West → right → North → right → East → left → North → right → East.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='cube box of volume 1,000 cm³ · cloth to cover all faces',
         stem='A cube-shaped box is packed exactly with 1,000 cubes of edge 1 cm, in 10 equal layers. How much cloth is needed to cover all the faces of the box exactly?',
         opts=['600 cm²', '100 cm²', '400 cm²', '1,000 cm²'],
         hint='How many cubes are in one layer? What square does one layer make?',
         sol='One layer has 1,000 ÷ 10 = 100 cubes, which is a 10 × 10 square. With 10 layers the box is 10 cm tall, so each edge is 10 cm. Each face is 10 × 10 = 100 cm². 6 faces: 600 cm².'),
    dict(ch='6', scen='4 rounds of wire round a 25 by 15 m garden at ₹12 per m',
         stem='A rectangular garden is 25 m long and 15 m wide. It is fenced with 4 rounds of wire. Wire costs ₹12 per metre. What is the cost of the wire?',
         opts=['₹3,840', '₹960', '₹4,500', '₹1,920'],
         hint='One round of wire is the perimeter.',
         sol='Perimeter: 2 × (25 + 15) = 80 m. 4 rounds: 320 m. Cost: 320 × 12 = ₹3,840.'),
    dict(ch='6', scen='two right triangles with sides 5 and 12 joined along the 12 cm side',
         stem='Two identical right-angled triangles, each with shorter sides 5 cm and 12 cm, are joined along their 12 cm sides to make one big triangle. What is its area?',
         opts=['60 cm²', '30 cm²', '120 cm²', '65 cm²'],
         hint='Find the area of one small triangle first.',
         sol='One triangle: half of 5 × 12 = 30 cm². Two of them: 60 cm². Joining does not change the total area.'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='bar graph of monthly savings · biggest rise',
         fig=drawing(300, 200, bars([('Jan', 150), ('Feb', 250), ('Mar', 100), ('Apr', 300)], 300, 50, 'Savings (₹)')),
         stem='The bar graph shows Payal\'s savings each month. In which month did her savings go up the most compared with the month before?',
         opts=['April', 'February', 'March', 'January'],
         hint='Find the change from each month to the next.',
         sol='Jan → Feb: +₹100. Feb → Mar: −₹150 (it went down). Mar → Apr: +₹200. The biggest rise was in April.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='thunder heard 6 seconds after lightning at 0.34 km per second',
         stem='Sound travels about 0.34 km every second. Tushar hears thunder 6 seconds after he sees the lightning. About how far away is the storm?',
         opts=['2.04 km', '2.4 km', '20.4 km', '1.7 km'],
         hint='The light reaches him almost at once.',
         sol='Distance = speed × time = 0.34 × 6 = 2.04 km.'),
    dict(ch='9', scen='180 km at average 45 km/h with first 90 km in 1.5 h',
         stem='A trip of 180 km has an average speed of 45 km/h. The first 90 km took 1.5 hours. At what speed was the rest of the trip driven?',
         opts=['36 km/h', '45 km/h', '60 km/h', '40 km/h'],
         hint='Find the total time of the trip first.',
         sol='Total time: 180 ÷ 45 = 4 h. The rest took 4 − 1.5 = 2.5 h for 90 km. 90 ÷ 2.5 = 36 km/h.'),
    dict(ch='9', scen='train from 14:45 to 06:20 the next day',
         stem='A train leaves at 14:45 and reaches its station at 06:20 the next morning (24-hour times). How long is the journey?',
         opts=['15 h 35 min', '8 h 25 min', '16 h 35 min', '15 h 25 min'],
         hint='Count to midnight first.',
         sol='14:45 to midnight is 9 h 15 min. Midnight to 06:20 is 6 h 20 min. Total: 15 h 35 min.'),
    dict(ch='9', scen='trip ₹1,250 each for 36 students with ₹4,500 donated',
         stem='A school trip costs ₹1,250 per student for 36 students. A parent gives ₹4,500 towards the trip. The rest is shared equally by the students. How much does each student pay?',
         opts=['₹1,125', '₹1,250', '₹1,100', '₹1,025'],
         hint='Share the gift among the 36 students first.',
         sol='The gift saves each student 4,500 ÷ 36 = ₹125. Each pays 1,250 − 125 = ₹1,125.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='two interleaved doubling series 2 10 4 20 8 40',
         fig=cards([2, 10, 4, 20, 8, 40, '?'], size=36),
         stem='Two patterns are mixed together in this series. Which number comes next?',
         opts=['16', '80', '10', '32'],
         hint='Look at the 1st, 3rd and 5th numbers.',
         sol='The 1st, 3rd, 5th numbers are 2, 4, 8 (doubling). The 2nd, 4th, 6th are 10, 20, 40 (doubling). The 7th number continues the first pattern: 16.'),
    dict(ch='10', scen='26 January 2025 Sunday · day in 2024',
         stem='Republic Day, 26 January, was a Sunday in 2025. 2024 was a leap year. On which day of the week was Republic Day in 2024?',
         opts=['Friday', 'Saturday', 'Monday', 'Thursday'],
         hint='Between the two dates is a 29 February.',
         sol='From 26 January 2024 to 26 January 2025 there are 366 days, because February 2024 had 29 days. 366 = 52 weeks + 2 days. Going back 2 days from Sunday gives Friday.'),
    dict(ch='10', scen='three cards from 1 to 9 adding to 20 · possible odd count',
         stem='Seema picks 3 different cards from cards numbered 1 to 9. Their numbers add up to 20. Which of these is possible?',
         opts=['Exactly 2 odd cards', 'All 3 even cards', 'Exactly 1 odd card', 'All 3 odd cards'],
         hint='Is 20 odd or even? Also, what is the largest total of three even cards?',
         sol='An even total needs an even number of odd cards: 0 or 2. Three even cards give at most 4 + 6 + 8 = 18, which is less than 20. So she must have exactly 2 odd cards, for example 9 + 7 + 4 = 20.'),
    dict(ch='10', scen='2-digit numbers whose tens digit is greater than the ones digit',
         stem='How many 2-digit numbers have a tens digit that is greater than the ones digit, like 52?',
         opts=['45', '36', '54', '50'],
         hint='Count by the tens digit: 1 _, 2 _, 3 _, …',
         sol='Tens 1: ones 0 (1 number). Tens 2: 2 numbers. … Tens 9: 9 numbers. 1 + 2 + … + 9 = 45.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='multiples of 6 below 100 that are not multiples of 9',
         stem='How many multiples of 6 that are less than 100 are NOT multiples of 9?',
         opts=['11', '16', '10', '5'],
         hint='A multiple of 6 that is also a multiple of 9 is a multiple of 18.',
         sol='Multiples of 6 below 100: 6, 12, …, 96, which is 16. Multiples of 18 among them: 18, 36, 54, 72, 90, which is 5. 16 − 5 = 11.'),
    dict(ch='3+10', scen='series multiplying by 1.5 from 4',
         fig=cards(['4', '6', '9', '13.5', '?'], size=40),
         stem='Each number in this series is found from the one before in the same way. Which number comes next?',
         opts=['20.25', '18', '20.5', '19.5'],
         hint='Compare 6 with 4, and 9 with 6.',
         sol='Each number is 1.5 times the one before: 4 × 1.5 = 6, 6 × 1.5 = 9, 9 × 1.5 = 13.5. Next: 13.5 × 1.5 = 13.5 + 6.75 = 20.25.'),
    dict(ch='6+10', scen='boxes of size n by n+1 by n+2 · first box over 500 cm³',
         stem='Kirti makes cuboid boxes. The 1st is 1 × 2 × 3 cm, the 2nd is 2 × 3 × 4 cm, the 3rd is 3 × 4 × 5 cm, and so on. Which is the first box with a volume of more than 500 cm³?',
         opts=['7th', '6th', '8th', '5th'],
         hint='Write the volumes of the 5th, 6th and 7th boxes.',
         sol='5th: 5 × 6 × 7 = 210 cm³. 6th: 6 × 7 × 8 = 336 cm³. 7th: 7 × 8 × 9 = 504 cm³. The 7th box is the first over 500 cm³.'),
    dict(ch='1+9', scen='bag CDXL and shoes DCCL paid with three ₹500 notes',
         stem='A shop shows prices in Roman numerals. A bag costs ₹CDXL and a pair of shoes costs ₹DCCL. Rahul buys both and pays with three ₹500 notes. How much change does he get?',
         opts=['₹310', '₹410', '₹290', '₹1,190'],
         hint='CD = 400 and DCC = 700.',
         sol='CDXL = 440 and DCCL = 750. Total: ₹1,190. He pays ₹1,500. Change: 1,500 − 1,190 = ₹310.'),
    dict(ch='3+9', scen='scooter 48.5 km per litre on three quarters of a 6 L tank',
         stem='A scooter goes 48.5 km on 1 litre of petrol. Its tank holds 6 litres. How far can it go on 3/4 of a full tank?',
         opts=['218.25 km', '291 km', '194 km', '220.25 km'],
         hint='Find 3/4 of 6 litres first.',
         sol='3/4 of 6 L = 4.5 L. Distance: 4.5 × 48.5 = 194 + 24.25 = 218.25 km.'),
]
