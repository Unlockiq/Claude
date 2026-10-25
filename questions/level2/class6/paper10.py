# AMO Level-2 · Class 6 · Practice Paper 10


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


def mid_square():
    return [('rect', 10, 10, 120, 120, 'yellow'), ('poly', [(70, 10), (130, 70), (70, 130), (10, 70)], 'blue'),
            ('text', 70, 146, '10 cm', 11)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='smallest 8-digit number with digit sum 9',
         stem='What is the smallest 8-digit number whose digits add up to 9?',
         opts=['1,00,00,008', '1,00,00,080', '1,00,00,009', '8,00,00,001'],
         hint='The first digit must be at least 1. Put the rest of the total as far right as possible.',
         sol='The first digit is 1, leaving 8 for the other digits. To keep the number small, put the 8 in the ones place: 1,00,00,008. (1,00,00,009 has digit sum 10.)'),
    dict(ch='1', scen='two numbers under 72 with LCM 72 and HCF 12 · their sum',
         stem='Two numbers, both less than 72, have LCM 72 and HCF 12. What is their sum?',
         opts=['60', '84', '48', '72'],
         hint='Both numbers are multiples of 12, and their product is 12 × 72.',
         sol='Write them as 12a and 12b with a and b sharing no factor, so a × b = 72 ÷ 12 = 6. The choices are 1 and 6 (12 and 72, but 72 is not less than 72) or 2 and 3 (24 and 36). Sum 24 + 36 = 60.'),
    dict(ch='1', scen='quiz with +4 correct −2 wrong 20 attempted scoring 50',
         stem='In a quiz, each correct answer gets +4, each wrong answer −2 and each skipped question 0. Isha attempts 20 of the 25 questions and scores 50. How many did she get wrong?',
         opts=['5', '15', '10', '3'],
         hint='If all 20 were correct she would score 80. Each wrong answer instead loses 6.',
         sol='All 20 correct would give 80. Each wrong answer changes +4 into −2, a loss of 6. 80 − 50 = 30 lost, so 30 ÷ 6 = 5 wrong. Check: 15 × 4 − 5 × 2 = 50.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='−48 over curly −2 times square 3 minus −1 plus 5',
         stem='What is the value of (−48) ÷ {(−2) × [3 − (−1)]} + 5?',
         opts=['11', '−1', '1', '17'],
         hint='Work out the square bracket, then the curly bracket.',
         sol='[3 − (−1)] = 4. {(−2) × 4} = −8. (−48) ÷ (−8) = 6. 6 + 5 = 11.'),
    dict(ch='2', scen='compare −7 times −8 minus −6 times 9 with −100 over −4 times 5',
         stem='Compare P = (−7) × (−8) − (−6) × 9 and Q = (−100) ÷ (−4) × 5. Which is true?',
         opts=['Q is larger, by 15', 'P is larger, by 15', 'P and Q are equal', 'Q is larger, by 235'],
         hint='In Q, divide first and then multiply, working left to right.',
         sol='P = 56 − (−54) = 56 + 54 = 110. Q = 25 × 5 = 125. Q is larger by 15.'),
    dict(ch='2', scen='A over B −4 and B over C −3 · A over C',
         stem='Three integers A, B and C have A ÷ B = −4 and B ÷ C = −3. What is A ÷ C?',
         opts=['12', '−12', '−7', '7'],
         hint='A = −4 × B and B = −3 × C.',
         sol='A = −4 × B = −4 × (−3 × C) = 12 × C. So A ÷ C = 12. Example: C = 1, B = −3, A = 12.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='how many of five forms equal 7/8',
         stem='How many of these are equal to 7/8: 0.875, 87.5%, 35/40, 21/24, 0.78?',
         opts=['4', '3', '5', '2'],
         hint='7/8 = 0.875.',
         sol='0.875 ✓. 87.5% = 0.875 ✓. 35/40 = 7/8 ✓. 21/24 = 7/8 ✓. 0.78 is not. So 4.'),
    dict(ch='3', scen='score from 40 to 50 and back · difference of the two percentages',
         stem='A batter\'s score rises from 40 to 50 in one match and falls from 50 to 40 in the next. The rise is a% and the fall is b%. What is a − b?',
         opts=['5', '0', '10', '20'],
         hint='Each percentage is worked out from the starting score of that change.',
         sol='Rise: 10 out of 40 = 25%. Fall: 10 out of 50 = 20%. a − b = 25 − 20 = 5.'),
    dict(ch='3', scen='15 L salt solution 20% salt plus 5 L water',
         stem='A 15-litre solution is 20% salt. 5 litres of water are added. What percentage of the new solution is salt?',
         opts=['15%', '20%', '25%', '12%'],
         hint='The amount of salt does not change.',
         sol='Salt = 20% of 15 = 3 L. New total = 20 L. 3/20 = 15/100 = 15%.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='hens and cows with 30 heads and 74 legs',
         stem='A farm has h hens and c cows. The total number of legs is 2h + 4c. There are 30 heads and 74 legs. How many cows are there?',
         opts=['7', '23', '14', '8'],
         hint='If all 30 animals were hens, there would be 60 legs.',
         sol='30 hens would have 60 legs. Each cow adds 2 more legs. 74 − 60 = 14 extra legs, so 14 ÷ 2 = 7 cows (and 23 hens).'),
    dict(ch='4', scen='m cubed minus 3mn plus n squared at m −1 n 2',
         stem='What is the value of m × m × m − 3 × m × n + n × n when m = −1 and n = 2?',
         opts=['9', '−3', '3', '−9'],
         hint='Work out each part with its sign: m × m × m is negative here.',
         sol='m × m × m = (−1)(−1)(−1) = −1. 3 × m × n = 3 × (−1) × 2 = −6. n × n = 4. Total: −1 − (−6) + 4 = 9.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='angles x plus 20 2x minus 10 and x plus 10 on a straight line',
         stem='Three angles on a straight line are (x + 20)°, (2x − 10)° and (x + 10)°. What is the smallest of the three angles?',
         opts=['50°', '40°', '60°', '70°'],
         hint='The three angles add up to 180°.',
         sol='(x + 20) + (2x − 10) + (x + 10) = 4x + 20 = 180, so x = 40. The angles are 60°, 70° and 50°. The smallest is 50°. (40° is x, not an angle.)'),
    dict(ch='5', scen='isosceles triangle with one angle three times another',
         stem='An isosceles triangle has one angle three times another of its angles. Which of these could be its angles?',
         opts=['36°, 36°, 108°', '45°, 45°, 90°', '30°, 30°, 120°', '60°, 60°, 60°'],
         hint='Check two things for each set: the sum is 180° and one angle is three times another.',
         sol='36° + 36° + 108° = 180° and 108° = 3 × 36°. ✓ In 45, 45, 90 the ratio is 2; in 30, 30, 120 it is 4; in 60, 60, 60 it is 1.'),
    dict(ch='5', scen='regular polygon with 20 diagonals and perimeter 64 · side',
         stem='A regular polygon has 20 diagonals and a perimeter of 64 cm. How long is each side?',
         opts=['8 cm', '10 cm', '6.4 cm', '16 cm'],
         hint='Find the number of sides from n × (n − 3) ÷ 2 = 20.',
         sol='n = 8: 8 × 5 ÷ 2 = 20 diagonals. ✓ So it is an octagon, and each side is 64 ÷ 8 = 8 cm.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='3 cm squares cut from the corners of a 15 by 10 rectangle',
         stem='A square of side 3 cm is cut from each corner of a 15 cm by 10 cm card. What are the area and the perimeter of the card that is left?',
         opts=['114 cm²; 50 cm', '114 cm²; 38 cm', '141 cm²; 50 cm', '114 cm²; 62 cm'],
         hint='Does cutting a square from a corner change the perimeter?',
         sol='Area: 150 − 4 × 9 = 114 cm². At each corner, two 3 cm edges are removed and two new 3 cm edges appear, so the perimeter stays 2 × (15 + 10) = 50 cm.'),
    dict(ch='6', scen='books 20 by 15 by 5 packed in a 40 by 30 by 20 box',
         stem='A box is 40 cm × 30 cm × 20 cm. Books 20 cm × 15 cm × 5 cm are packed flat in it, all the same way up. How many books fit?',
         opts=['16', '32', '8', '24'],
         hint='Count how many fit along each edge.',
         sol='Along 40: 2 books. Along 30: 2 books. Up 20 cm: 4 books of 5 cm. 2 × 2 × 4 = 16. (The volumes give 24,000 ÷ 1,500 = 16 too.)'),
    dict(ch='6', scen='cuboid with edges totalling 72 cm length 8 breadth 6 · volume',
         stem='All 12 edges of a cuboid add up to 72 cm. Its length is 8 cm and its breadth is 6 cm. What is its volume?',
         opts=['192 cm³', '288 cm³', '336 cm³', '144 cm³'],
         hint='A cuboid has 4 edges of each length.',
         sol='4 × (8 + 6 + h) = 72, so 8 + 6 + h = 18 and h = 4 cm. Volume = 8 × 6 × 4 = 192 cm³.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='students absent bar graph · days with attendance above 85% of 40',
         fig=drawing(330, 210, bars([('Mon', 6), ('Tue', 3), ('Wed', 9), ('Thu', 4), ('Fri', 8)], 10, 1, 'Students absent (class of 40)')),
         stem='The bar graph shows how many students of a class of 40 were absent each day. On how many days was the attendance above 85%?',
         opts=['2', '3', '1', '4'],
         hint='Above 85% present means fewer than how many absent?',
         sol='85% of 40 = 34, so attendance above 85% means more than 34 present, that is fewer than 6 absent. Tuesday (3) and Thursday (4): 2 days. Monday has exactly 6 absent, which is exactly 85%.'),
    dict(ch='8', scen='runs in ten innings table · total and innings of 40 or more',
         fig=table(['Runs in an innings', '0', '10', '25', '40', '50'], [['Innings', '1', '2', '3', '2', '2']], widths=[140, 45, 45, 45, 45, 45]),
         stem='The table shows the runs Kunal scored in his 10 innings. How many runs did he score in all, and in how many innings did he score 40 or more?',
         opts=['275; 4 innings', '275; 2 innings', '125; 4 innings', '300; 4 innings'],
         hint='Multiply each score by its number of innings.',
         sol='Total: 0 + 20 + 75 + 80 + 100 = 275. Innings with 40 or more: 2 + 2 = 4.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='dog running between two walkers 18 km apart',
         stem='Two friends 18 km apart walk towards each other at 4 km/h and 5 km/h. A dog runs back and forth between them at 12 km/h until they meet. How far does the dog run?',
         opts=['24 km', '18 km', '12 km', '36 km'],
         hint='Do not follow the dog\'s trips. Find how long it runs.',
         sol='The friends close the gap at 9 km/h, so they meet after 18 ÷ 9 = 2 hours. The dog runs for 2 hours at 12 km/h: 24 km.'),
    dict(ch='9', scen='salaries 4:5 becoming 5:6 after ₹2,000 rise each',
         stem='The salaries of Ankita and Bhuvan are in the ratio 4 : 5. Each gets a rise of ₹2,000 and the ratio becomes 5 : 6. What was Ankita\'s salary before the rise?',
         opts=['₹8,000', '₹10,000', '₹4,000', '₹12,000'],
         hint='Try the options: check both ratios.',
         sol='Ankita ₹8,000 and Bhuvan ₹10,000 are in the ratio 4 : 5. After the rise: 10,000 : 12,000 = 5 : 6. ✓'),
    dict(ch='9', scen='typist 1,200 words in 25 minutes · words in 1 h 15 min',
         stem='A typist types 1,200 words in 25 minutes. At the same speed, how many words does she type in 1 hour 15 minutes?',
         opts=['3,600', '3,000', '4,800', '2,400'],
         hint='1 hour 15 minutes = 75 minutes.',
         sol='75 minutes = 3 × 25 minutes. 3 × 1,200 = 3,600 words.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='1,000 minutes after 9:20 AM',
         stem='What time is it exactly 1,000 minutes after 9:20 AM?',
         opts=['2:00 AM', '1:00 AM', '2:00 PM', '1:40 AM'],
         hint='1,000 minutes = how many hours and minutes?',
         sol='1,000 = 16 × 60 + 40, so 16 h 40 min. 9:20 AM + 16 h = 1:20 AM next day. 40 min more: 2:00 AM.'),
    dict(ch='10', scen='nine people each shaking hands with exactly three others',
         stem='Can each of 9 people shake hands with exactly 3 of the others?',
         opts=['No, because 9 × 3 is odd', 'Yes, in many ways', 'Yes, but in only one way', 'No, because 9 is a multiple of 3'],
         hint='Each handshake involves two people.',
         sol='Counting handshakes person by person gives 9 × 3 = 27, and this counts every handshake twice, so it must be even. 27 is odd, so it is impossible.'),
    dict(ch='10', scen='stickers: quarter given away then 6 more then half the rest',
         stem='Meena gives away a quarter of her stickers, then 6 more, then half of what is left. She has 15 left. How many did she have at first?',
         opts=['48', '40', '52', '60'],
         hint='Work backwards: double, add 6, and then find the whole from three quarters.',
         sol='Before the last step: 15 × 2 = 30. Before giving 6: 36. That is 3/4 of the start, so she had 36 ÷ 3 × 4 = 48.'),

    # ---------------- Mixed Problems
    dict(ch='4+10', scen='first n with 1 plus 2 up to n above 200',
         stem='The sum 1 + 2 + 3 + … + n equals n × (n + 1) ÷ 2. What is the smallest n for which the sum is more than 200?',
         opts=['20', '19', '21', '14'],
         hint='Try n = 19 and n = 20.',
         sol='n = 19: 19 × 20 ÷ 2 = 190, not enough. n = 20: 20 × 21 ÷ 2 = 210 > 200. So n = 20.'),
    dict(ch='1+10', scen='numbers 1 to 200 divisible by 4 or 6 but not both',
         stem='How many numbers from 1 to 200 are divisible by 4 or by 6, but not by both?',
         opts=['51', '67', '83', '34'],
         hint='Numbers divisible by both are multiples of 12.',
         sol='Multiples of 4: 50. Multiples of 6: 33. Multiples of 12 (both): 16. Only 4: 50 − 16 = 34. Only 6: 33 − 16 = 17. Total 34 + 17 = 51.'),
    dict(ch='3+9', scen='customers 25% up on Saturday then 20% down on Sunday',
         stem='A shop had 160 customers on Friday. Saturday had 25% more customers than Friday, and Sunday had 20% fewer than Saturday. How many customers came on Sunday?',
         opts=['160', '168', '152', '200'],
         hint='Work out Saturday first.',
         sol='Saturday: 160 + 25% of 160 = 200. Sunday: 200 − 20% of 200 = 160. (168 wrongly treats it as a 5% rise.)'),
    dict(ch='5+6', scen='square joining the midpoints of a 10 cm square · area',
         fig=drawing(140, 150, mid_square()),
         stem='A square is drawn by joining the midpoints of the sides of a square of side 10 cm, as shown. What is the area of the inner square?',
         opts=['50 cm²', '25 cm²', '75 cm²', '40 cm²'],
         hint='The four corner pieces are right-angled triangles with shorter sides of 5 cm.',
         sol='Each corner triangle has area 5 × 5 ÷ 2 = 12.5 cm². Four of them: 50 cm². Inner square = 100 − 50 = 50 cm².'),
    dict(ch='4+9', scen='plant 12 cm growing 3 cm a week against plant 30 cm growing 1.5 cm',
         stem='Plant A is 12 cm tall and grows 3 cm a week. Plant B is 30 cm tall and grows 1.5 cm a week. After how many weeks are they the same height?',
         opts=['12 weeks', '6 weeks', '8 weeks', '18 weeks'],
         hint='Plant A catches up by 1.5 cm each week.',
         sol='The gap is 18 cm and closes by 3 − 1.5 = 1.5 cm a week. 18 ÷ 1.5 = 12 weeks. Both are then 48 cm.'),
]
