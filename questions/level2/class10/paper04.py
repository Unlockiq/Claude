# AMO Level-2 · Class 10 · Practice Paper 4  (format: see paper01.py)


def concentric():
    import math
    O = (90, 90)
    R, r = 75, 45
    y = O[1] + r
    dx = math.sqrt(R * R - r * r)
    return [('circle', O[0], O[1], R, None), ('circle', O[0], O[1], r, 'yellow'), ('line', O[0] - dx, y, O[0] + dx, y),
            ('line', O[0], O[1], O[0], y, True), ('line', O[0], O[1], O[0] + dx, y, True), ('dot', O[0], O[1], 3),
            ('text', O[0] - 10, O[1] - 6, 'O', 12), ('text', O[0] - dx - 10, y + 6, 'A', 12), ('text', O[0] + dx + 10, y + 6, 'B', 12),
            ('text', O[0] - 10, y + 12, 'M', 12)]



def concentric_diameter():
    import math
    O = (90, 90)
    R, r = 75, 45
    y = O[1] + r
    dx = math.sqrt(R * R - r * r)
    A, B, M = (O[0] - dx, y), (O[0] + dx, y), (O[0], y)
    E = (2 * O[0] - A[0], 2 * O[1] - A[1])
    return [('circle', O[0], O[1], R, None), ('circle', O[0], O[1], r, 'yellow'), ('line', A[0], A[1], B[0], B[1]),
            ('line', A[0], A[1], E[0], E[1]), ('line', M[0], M[1], E[0], E[1], True), ('dot', O[0], O[1], 3),
            ('text', O[0] - 12, O[1] - 4, 'O', 12), ('text', A[0] - 10, A[1] + 6, 'A', 12), ('text', B[0] + 10, B[1] + 6, 'B', 12),
            ('text', M[0], M[1] + 13, 'M', 12), ('text', E[0] + 8, E[1] - 8, 'E', 12)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='smallest multiple of 7 leaving remainder 5 on division by 12 15 and 20',
         stem='What is the smallest number that leaves a remainder of 5 when divided by 12, by 15 and by 20, and is also divisible by 7?',
         opts=['245', '65', '125', '185'],
         hint='Such numbers are 5 more than a multiple of LCM(12, 15, 20).',
         sol='LCM = 60, so the number is 60k + 5: 65, 125, 185, 245, … Testing for 7: 65, 125 and 185 are not multiples of 7, but 245 = 7 × 35. So 245.'),
    dict(ch='1', scen='last digit of 7 to the power 2026',
         stem='What is the last digit of 7²⁰²⁶?',
         opts=['9', '7', '1', '3'],
         hint='The last digits of 7¹, 7², 7³, 7⁴ repeat in a cycle.',
         sol='Last digits go 7, 9, 3, 1, then repeat every 4. 2026 = 4 × 506 + 2, so the last digit is the 2nd in the cycle: 9.'),

    # ---------------- Part 2 · Fractions, Decimals & Percentages
    dict(ch='3', scen='rate that turns ₹6,250 into ₹7,290 in two years',
         stem='At what rate of compound interest per annum (compounded yearly) will ₹6,250 amount to ₹7,290 in 2 years?',
         opts=['8%', '8.32%', '9%', '7%'],
         hint='7,290/6,250 is a perfect square of a simple decimal.',
         sol='(1 + r/100)² = 7,290/6,250 = 1.1664 = 1.08². So r = 8%. (8.32% is the simple-interest rate for the same gain.)'),
    dict(ch='3', scen='interest of ₹1,320 in year two and ₹1,452 in year three',
         stem='On a sum at compound interest (compounded yearly), the interest for the 2nd year is ₹1,320 and for the 3rd year is ₹1,452. What is the sum?',
         opts=['₹12,000', '₹13,200', '₹10,000', '₹11,000'],
         hint='The 3rd year\'s interest is the 2nd year\'s interest plus interest on it.',
         sol='1,452 ÷ 1,320 = 1.1, so the rate is 10%. Interest in year 2 = P × 1.1 × 0.1 = 0.11P = 1,320, so P = ₹12,000.'),
    dict(ch='3', scen='town population up 10 then 20 then down 25 percent',
         stem='The population of a town rises by 10% in one year and by 20% the next year. In the third year it falls by 25%. What is the overall change over the three years?',
         opts=['1% decrease', '5% increase', 'No change', '1% increase'],
         hint='Multiply the growth factors.',
         sol='1.1 × 1.2 × 0.75 = 0.99. The population is 99% of the start: a 1% decrease. (Adding 10 + 20 − 25 = 5 is wrong.)'),

    # ---------------- Part 3 · Algebra
    dict(ch='4', scen='k when the zeros of x² − 12x + k differ by 6',
         stem='The zeros of x² − 12x + k differ by 6. What is k?',
         opts=['27', '35', '32', '36'],
         hint='(α − β)² = (α + β)² − 4αβ.',
         sol='α + β = 12 and αβ = k. (α − β)² = 144 − 4k = 36, so 4k = 108 and k = 27. The zeros are 9 and 3. (36 gives equal zeros; 32 gives zeros 8 and 4; 35 gives 7 and 5.)'),
    dict(ch='4', scen='three batters scoring 120 runs with two conditions',
         stem='Anaya, Kabir and Riya scored 120 runs in all. Anaya scored 10 more than Kabir. Riya scored 20 fewer than Anaya and Kabir together. How many runs did Riya score?',
         opts=['50', '40', '30', '60'],
         hint='Write each score in terms of Kabir\'s score k.',
         sol='Anaya = k + 10 and Riya = (2k + 10) − 20 = 2k − 10. Total: k + 10 + k + 2k − 10 = 4k = 120, so k = 30. Riya = 50.'),
    dict(ch='4', scen='number of terms of 24 21 18 giving a zero sum',
         stem='How many terms of the AP 24, 21, 18, … must be added to get a sum of 0?',
         opts=['17', '16', '9', '8'],
         hint='Sₙ = n/2 × (2a + (n − 1)d) = 0 with n ≠ 0.',
         sol='2 × 24 + (n − 1)(−3) = 0 gives n − 1 = 16, so n = 17. The positive terms 24 to 3 cancel the negative terms −3 to −24 after the 0.'),
    dict(ch='4', scen='number exceeding its reciprocal by 24/5 · square plus reciprocal square',
         stem='A positive number x exceeds its reciprocal by 24/5. What is x² + 1/x²?',
         opts=['626/25', '576/25', '526/25', '26'],
         hint='Square x − 1/x = 24/5 instead of solving for x.',
         sol='(x − 1/x)² = x² − 2 + 1/x². So x² + 1/x² = (24/5)² + 2 = 576/25 + 50/25 = 626/25. (Check: x = 5 gives 25 + 1/25 = 626/25.)'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='perimeters of two similar triangles with areas 81 and 49 adding to 64',
         stem='The areas of two similar triangles are 81 cm² and 49 cm². The sum of their perimeters is 64 cm. What is the perimeter of the larger triangle?',
         opts=['36 cm', '28 cm', '32 cm', '40.5 cm'],
         hint='The ratio of areas is the square of the ratio of sides.',
         sol='Ratio of sides = √(81/49) = 9/7, and perimeters are in the same ratio. Larger = 64 × 9/16 = 36 cm. (40.5 cm uses 81 : 49 directly.)'),
    dict(ch='5', scen='chord touching the inner of two concentric circles · distance from M to the far end of diameter AE',
         fig=drawing(180, 175, concentric_diameter()),
         stem='Two concentric circles with centre O have radii 5 cm and 3 cm. A chord AB of the larger circle touches the smaller circle at M. AO is extended to meet the larger circle again at E. What is the length ME?',
         opts=['2√13 cm', '8 cm', '√34 cm', '6 cm'],
         hint='O is the midpoint of AE and M is the midpoint of AB. Use the midpoint theorem in triangle ABE.',
         sol='OM ⊥ AB, so AM = MB = √(25 − 9) = 4 cm. In triangle ABE, O and M are midpoints of AE and AB, so BE = 2 × OM = 6 cm and BE ∥ OM, making angle ABE = 90°. ME = √(MB² + BE²) = √(16 + 36) = √52 = 2√13 cm.'),
    dict(ch='5', scen='points of trisection of the segment from (−2, 3) to (4, −3)',
         stem='The two points that divide the segment from (−2, 3) to (4, −3) into three equal parts are found. What is the sum of all four of their coordinates?',
         opts=['2', '0', '1', '4'],
         hint='Use the section formula with ratios 1 : 2 and 2 : 1.',
         sol='Ratio 1 : 2: ((4 − 4)/3, (−3 + 6)/3) = (0, 1). Ratio 2 : 1: ((8 − 2)/3, (−6 + 3)/3) = (2, −1). Sum = 0 + 1 + 2 − 1 = 2.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='surface area of a capsule 14 mm long and 5 mm wide',
         stem='A medicine capsule is a cylinder with a hemisphere at each end. Its total length is 14 mm and its diameter is 5 mm. What is its surface area? (Take π = 22/7.)',
         opts=['220 mm²', '141 mm²', '298 mm²', '176 mm²'],
         hint='The cylinder part is 14 − 5 = 9 mm long.',
         sol='Cylinder CSA = 2 × 22/7 × 2.5 × 9 = 990/7. Two hemispheres = 4 × 22/7 × 2.5² = 550/7. Total = 1,540/7 = 220 mm².'),
    dict(ch='6', scen='hemispherical bowl of radius 9 poured into small cylindrical bottles',
         stem='A hemispherical bowl of inner radius 9 cm is full of juice. It is poured into cylindrical bottles of radius 1.5 cm and height 4 cm. How many bottles can be filled?',
         opts=['54', '81', '27', '108'],
         hint='Hemisphere volume = (2/3)πr³.',
         sol='Bowl = (2/3)π × 729 = 486π cm³. One bottle = π × 2.25 × 4 = 9π cm³. 486 ÷ 9 = 54 bottles. (108 uses a full sphere.)'),
    dict(ch='6', scen='60 degree sector with perimeter 64 cm · its area',
         stem='A sector of a circle has an angle of 60° at the centre and a perimeter of 64 cm. What is its area? (Take π = 22/7.)',
         opts=['231 cm²', '462 cm²', '22 cm²', '1386 cm²'],
         hint='Perimeter = 2r + arc length. Find r first.',
         sol='Arc = (60/360) × 2 × 22/7 × r = 22r/21. So 2r + 22r/21 = 64r/21 = 64, giving r = 21 cm. Area = (1/6) × 22/7 × 441 = 231 cm². (1386 cm² is the whole circle.)'),

    # ---------------- Part 6 · Trigonometry
    dict(ch='7', scen='sin theta plus cos theta equals root 2 cos theta · tan theta',
         stem='For an acute angle θ, sin θ + cos θ = √2 cos θ. What is tan θ, and what is the value of tan θ + cot θ?',
         opts=['√2 − 1 and 2√2', '√2 + 1 and 2√2', '√2 − 1 and 2', '1 and 2'],
         hint='Divide both sides by cos θ.',
         sol='Dividing by cos θ: tan θ + 1 = √2, so tan θ = √2 − 1. Then cot θ = 1/(√2 − 1) = √2 + 1. tan θ + cot θ = 2√2.'),
    dict(ch='7', scen='kite string of 60 m changing from 60 to 45 degrees',
         stem='A kite is on a straight string 60 m long making 60° with the level ground. The wind changes and the string, still 60 m long, now makes 45°. By how much has the kite come down?',
         opts=['30(√3 − √2) m', '30√3 m', '30√2 m', '15 m'],
         hint='Height = 60 × sin of the angle.',
         sol='Heights: 60 sin 60° = 30√3 m and 60 sin 45° = 30√2 m. Drop = 30√3 − 30√2 = 30(√3 − √2) m (about 9.5 m).'),

    # ---------------- Part 7 · Data Handling, Statistics & Probability
    dict(ch='8', scen='median from a less-than cumulative frequency table',
         fig=table(['Marks less than', '10', '20', '30', '40', '50'], [['Students', '4', '11', '26', '34', '40']], widths=[120, 56, 56, 56, 56, 56]),
         stem='The table gives a cumulative frequency distribution of marks. What is the median mark?',
         opts=['26', '25', '27.5', '30'],
         hint='Turn the cumulative frequencies back into class frequencies.',
         sol='Class frequencies: 4, 7, 15, 8, 6, with N = 40 and N/2 = 20. The median class is 20–30 (cf before it = 11, f = 15). Median = 20 + ((20 − 11)/15) × 10 = 26.'),
    dict(ch='8', scen='two balls of the same colour from 5 red and 3 blue without replacement',
         stem='A bag has 5 red and 3 blue balls. Two balls are drawn one after the other without replacement. What is the probability that both are the same colour?',
         opts=['13/28', '17/32', '5/14', '1/2'],
         hint='Add P(both red) and P(both blue).',
         sol='P(both red) = 5/8 × 4/7 = 20/56. P(both blue) = 3/8 × 2/7 = 6/56. Total 26/56 = 13/28. (17/32 assumes the first ball is put back.)'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='buy three get one free plus 10 percent off the bill',
         stem='A shop offers "buy 3, get 1 free" on shirts of the same price, and then 10% off the bill. What is the effective discount on 4 shirts?',
         opts=['32.5%', '35%', '25%', '40%'],
         hint='Take each shirt as ₹100.',
         sol='4 shirts worth ₹400 cost 3 × 100 = ₹300, then 10% off: ₹270. Discount = 130/400 = 32.5%. (35% adds 25% and 10%.)'),
    dict(ch='9', scen='three workers in pairs taking 12 15 and 20 days',
         stem='Hema and Raghav can do a job in 12 days, Raghav and Sneha in 15 days, and Hema and Sneha in 20 days. How long would Hema take alone?',
         opts=['30 days', '20 days', '60 days', '24 days'],
         hint='Adding all three pair rates counts each person twice.',
         sol='2(H + R + S) = 1/12 + 1/15 + 1/20 = 1/5, so H + R + S = 1/10. H = 1/10 − (R + S) = 1/10 − 1/15 = 1/30. Hema takes 30 days.'),
    dict(ch='9', scen='dealer buying and selling within the state · CGST paid after input credit',
         stem='A dealer in Pune buys goods for ₹10,000 plus 18% GST and sells them in Mumbai for ₹12,000 plus 18% GST. Both deals are within the state. After input tax credit, how much CGST does the dealer pay to the government?',
         opts=['₹180', '₹360', '₹1,080', '₹90'],
         hint='Net GST = GST collected on the sale − GST paid on the purchase. CGST is half of it.',
         sol='GST collected = 18% of 12,000 = ₹2,160. GST paid = 18% of 10,000 = ₹1,800. Net GST = ₹360, shared equally as CGST and SGST: CGST = ₹180. (₹360 is the total net GST.)'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='points in a 2 by 2 square forcing two within root 2',
         stem='Points are placed in a square of side 2 cm (inside it or on its edges). What is the least number of points that guarantees two of them are at most √2 cm apart?',
         opts=['5', '4', '9', '3'],
         hint='Cut the square into four 1 cm × 1 cm squares.',
         sol='Each small square has diagonal √2, so two points in the same small square are at most √2 apart. With 5 points, two share a small square. With 4 points at the corners, all distances are at least 2.'),
    dict(ch='10', scen='handshakes among five couples who do not shake their own partner',
         stem='At a party there are 5 couples. Everyone shakes hands once with every other person except their own partner. How many handshakes take place?',
         opts=['40', '45', '35', '90'],
         hint='Count all possible handshakes among 10 people, then remove the forbidden ones.',
         sol='Each of the 10 people shakes hands with everyone except themselves and their partner, that is with 8 people. 10 × 8 = 80 counts every handshake twice (once for each person), so there are 40 handshakes. (45 forgets that partners do not shake hands.)'),
    dict(ch='10', scen='splitting 10 into positive integers with the largest product',
         stem='The number 10 is written as a sum of positive integers, such as 4 + 6 or 2 + 3 + 5. What is the largest possible product of the parts?',
         opts=['36', '32', '30', '25'],
         hint='Parts of 4 or more can be split to increase the product; 1s never help.',
         sol='Use as many 3s as possible: 10 = 3 + 3 + 2 + 2 gives 36 (3 + 3 + 4 also gives 36). Five 2s give 32 and 5 + 5 gives 25. So 36.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='perfect squares among the terms of 3 7 11 below 1000',
         stem='How many terms of the AP 3, 7, 11, 15, … that are less than 1000 are perfect squares?',
         opts=['0', '15', '16', '31'],
         hint='What remainder does each term leave on division by 4? What remainders can squares leave?',
         sol='Every term is 4k + 3, so it leaves remainder 3 on division by 4. A square leaves remainder 0 (even number) or 1 (odd number). So no term is a perfect square.'),
    dict(ch='5+7', scen='chord subtending 120 degrees in a circle of radius 10',
         stem='A chord of a circle of radius 10 cm subtends an angle of 120° at the centre. What is the length of the chord?',
         opts=['10√3 cm', '10 cm', '5√3 cm', '20 cm'],
         hint='The perpendicular from the centre bisects the chord and the angle.',
         sol='Half the chord = 10 sin 60° = 5√3 cm. Chord = 10√3 cm (about 17.3 cm).'),
    dict(ch='4+5', scen='(3, a) dividing the segment from (1, 2) to (b, 8) in the ratio 1 : 2',
         stem='The point (3, a) divides the segment joining (1, 2) and (b, 8) in the ratio 1 : 2. What is a + b?',
         opts=['11', '9', '13', '10'],
         hint='By the section formula the point is ((1 × b + 2 × 1)/3, (1 × 8 + 2 × 2)/3).',
         sol='x: (b + 2)/3 = 3 gives b = 7. y: (8 + 4)/3 = 4, so a = 4. a + b = 11.'),
    dict(ch='3+9', scen='half-yearly 10 percent loan against 10.2 percent simple interest',
         stem='Ankita needs a loan of ₹50,000 for 1 year. Bank P charges 10% per annum compounded half-yearly. Bank Q charges 10.2% per annum simple interest. Which bank is cheaper, and by how much?',
         opts=['Bank Q, by ₹25', 'Bank P, by ₹25', 'Bank Q, by ₹125', 'Both cost the same'],
         hint='Bank P charges 5% for each half-year.',
         sol='Bank P: 50,000 × 1.05² − 50,000 = ₹5,125. Bank Q: 10.2% of 50,000 = ₹5,100. Bank Q is cheaper by ₹25.'),
    dict(ch='6+10', scen='small cubes painted on exactly two faces from a painted 3 by 4 by 5 cuboid',
         stem='A cuboid 3 cm × 4 cm × 5 cm is painted on all faces and cut into 1 cm cubes. How many of the small cubes have paint on exactly two faces?',
         opts=['24', '22', '8', '6'],
         hint='Such cubes lie along the edges of the cuboid but not at the corners.',
         sol='A cuboid has 4 edges of each length. Leaving out the 2 corner cubes, the edges of length 3, 4 and 5 hold 1, 2 and 3 such cubes. Total 4 × (1 + 2 + 3) = 24. (8 cubes have three painted faces, 22 have one and 6 have none: 8 + 24 + 22 + 6 = 60.)'),
]
