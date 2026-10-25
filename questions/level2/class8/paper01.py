# AMO Level-2 · Class 8 · Practice Paper 1
# Each question: ch, scen (unique), stem, opts (correct FIRST), hint, sol, optional fig.


def hist(edges, freqs, top, step, xlab='', bw=46, h=150):
    """Histogram: adjacent bars over class intervals, y axis 0..top with gridlines every step."""
    x0, y0 = 40, 10
    w = len(freqs) * bw
    prims = []
    for v in range(0, top + 1, step):
        y = y0 + h - v * h / top
        prims += [('line', x0, y, x0 + w + 10, y, True, (170, 170, 170), 0.8), ('text', x0 - 16, y, str(v), 10)]
    for i, f in enumerate(freqs):
        x = x0 + i * bw
        prims.append(('rect', x, y0 + h - f * h / top, bw, f * h / top, 'blue'))
    for i, e in enumerate(edges):
        prims.append(('text', x0 + i * bw, y0 + h + 13, str(e), 10))
    prims += [('line', x0, y0, x0, y0 + h), ('line', x0, y0 + h, x0 + w + 10, y0 + h)]
    if xlab:
        prims.append(('text', x0 + w / 2, y0 + h + 30, xlab, 10))
    return prims


def sierp(n, x, y, s):
    """Sierpinski triangle at step n, apex (x, y), side s (shaded triangles only)."""
    h = s * 0.866
    if n == 0:
        return [('poly', [(x, y), (x - s / 2, y + h), (x + s / 2, y + h)], 'pink')]
    return sierp(n - 1, x, y, s / 2) + sierp(n - 1, x - s / 4, y + h / 2, s / 2) + sierp(n - 1, x + s / 4, y + h / 2, s / 2)


def sierp_steps():
    prims = []
    for k in range(3):
        cx = 50 + k * 120
        prims += [('poly', [(cx, 10), (cx - 45, 88), (cx + 45, 88)], 'white')] + sierp(k, cx, 10, 90)
        prims.append(('text', cx, 104, f'Step {k}', 11))
    return prims


def lamp():
    return [('line', 20, 10, 20, 150), ('text', 6, 80, '6 m', 11), ('dot', 20, 10, 5),
            ('line', 120, 112, 120, 150), ('text', 133, 128, '1.5 m', 10),
            ('line', 20, 10, 170, 150, True), ('line', 0, 150, 190, 150),
            ('text', 70, 162, '4 m', 11), ('text', 145, 162, 'shadow', 10)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='perfect squares between 50 and 400 that are multiples of 3',
         stem='How many perfect squares lie between 50 and 400 and are also multiples of 3?',
         opts=['4', '5', '6', '3'],
         hint='A perfect square is a multiple of 3 only when its square root is a multiple of 3.',
         sol='The squares between 50 and 400 are 8², 9², …, 19² (20² = 400 is not between). A square is a multiple of 3 exactly when its root is, so the roots are 9, 12, 15 and 18. That is 4 squares: 81, 144, 225 and 324.'),
    dict(ch='1', scen='x equals root 2 plus 1 · which expression is rational',
         stem='Let x = √2 + 1. Which of these numbers is rational?',
         opts=['x(x − 2)', 'x²', '2x − 1', 'x + √8'],
         hint='x − 2 = √2 − 1. Multiply it by x = √2 + 1.',
         sol='x(x − 2) = (√2 + 1)(√2 − 1) = 2 − 1 = 1, which is rational. x² = 3 + 2√2, 2x − 1 = 2√2 + 1 and x + √8 = 3√2 + 1 all contain √2, so they are irrational.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='solve 3 to the 2x minus 1 times 9 to the minus 2 equals 27 to the minus 1',
         stem='Find x if 3²ˣ⁻¹ × 9⁻² = 27⁻¹.',
         opts=['1', '2', '−1', '3'],
         hint='Write 9 and 27 as powers of 3.',
         sol='9⁻² = 3⁻⁴ and 27⁻¹ = 3⁻³. So 3²ˣ⁻¹⁻⁴ = 3⁻³, which gives 2x − 5 = −3, so 2x = 2 and x = 1.'),
    dict(ch='2', scen='distance from the Sun from light speed and 500 seconds in standard form',
         stem='Light travels 3 × 10⁸ metres every second. Sunlight takes about 500 seconds to reach the Earth. About how far is the Sun, in kilometres, in standard form?',
         opts=['1.5 × 10⁸ km', '1.5 × 10¹¹ km', '1.5 × 10⁵ km', '6 × 10⁵ km'],
         hint='First find the distance in metres, then divide by 1,000.',
         sol='3 × 10⁸ × 500 = 1,500 × 10⁸ = 1.5 × 10¹¹ m. In kilometres: 1.5 × 10¹¹ ÷ 10³ = 1.5 × 10⁸ km. (6 × 10⁵ comes from dividing by 500 instead of multiplying.)'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='successive 20 and 10 percent off against a single 30 percent off on ₹2,500',
         stem='A watch is marked ₹2,500. Shop P gives 20% off and then a further 10% off the reduced price. Shop Q gives a single 30% off. How much more does a buyer pay at shop P?',
         opts=['₹50', '₹0', '₹75', '₹25'],
         hint='Successive discounts are applied one after the other, on the reduced price.',
         sol='Shop P: 2,500 × 0.8 = 2,000, then 2,000 × 0.9 = ₹1,800. Shop Q: 2,500 × 0.7 = ₹1,750. Shop P costs ₹50 more. (20% + 10% is not the same as 30%.)'),
    dict(ch='3', scen='sum doubles in 8 years at simple interest · years to triple',
         stem='At simple interest, a sum of money doubles itself in 8 years. In how many years will it become three times itself at the same rate?',
         opts=['16', '24', '12', '20'],
         hint='Doubling means the interest equals the sum once.',
         sol='Doubling in 8 years means the interest in 8 years equals the principal, so the rate is 100 ÷ 8 = 12.5% a year. To triple, the interest must be twice the principal: 200% ÷ 12.5% = 16 years.'),
    dict(ch='3', scen='price up 20 then down 20 then up 25 percent · net change',
         stem='The price of a bicycle rises by 20%, then falls by 20%, and then rises by 25%. What is the overall change in the price?',
         opts=['20% increase', '25% increase', 'No change', '4% decrease'],
         hint='Multiply the factors: 1.2, 0.8 and 1.25.',
         sol='1.2 × 0.8 = 0.96, a 4% fall after two changes. 0.96 × 1.25 = 1.2. So the price is 1.2 times the original: a 20% increase.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='a plus b is 9 and ab is 14 · a squared plus b squared',
         stem='Two numbers a and b have a + b = 9 and ab = 14. What is a² + b²?',
         opts=['53', '81', '67', '25'],
         hint='Use (a + b)² = a² + 2ab + b².',
         sol='(a + b)² = 81 = a² + b² + 2 × 14. So a² + b² = 81 − 28 = 53. (Check: the numbers are 2 and 7, and 4 + 49 = 53.)'),
    dict(ch='4', scen='1001 squared minus 999 squared over 51 squared minus 49 squared',
         stem='Without long multiplication, find (1001² − 999²) ÷ (51² − 49²).',
         opts=['20', '2', '10', '40'],
         hint='Use a² − b² = (a + b)(a − b) on top and bottom.',
         sol='1001² − 999² = (2000)(2) = 4,000. 51² − 49² = (100)(2) = 200. 4,000 ÷ 200 = 20.'),
    dict(ch='4', scen='father four times son now and twice in 16 years',
         stem='Kunal\'s father is now 4 times as old as Kunal. In 16 years he will be twice as old as Kunal. How old is Kunal now?',
         opts=['8', '16', '12', '6'],
         hint='Let Kunal be x years old. Write both ages in 16 years.',
         sol='Now: x and 4x. In 16 years: x + 16 and 4x + 16. So 4x + 16 = 2(x + 16) = 2x + 32, giving 2x = 16 and x = 8. Check: 8 and 32 now; 24 and 48 later.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='13 m ladder sliding out from 5 m to 12 m · drop of the top',
         stem='A 13 m ladder leans against a wall with its foot 5 m from the wall. The foot slides out until it is 12 m from the wall. How far does the top of the ladder slide down?',
         opts=['7 m', '5 m', '12 m', '1 m'],
         hint='Use Pythagoras twice: once for each position.',
         sol='At first the top is √(13² − 5²) = √144 = 12 m high. Later it is √(13² − 12²) = √25 = 5 m high. It slides down 12 − 5 = 7 m.'),
    dict(ch='5', scen='rhombus with diagonals 16 and 30 · perimeter',
         stem='The diagonals of a rhombus are 16 cm and 30 cm long. What is the perimeter of the rhombus?',
         opts=['68 cm', '46 cm', '92 cm', '34 cm'],
         hint='The diagonals of a rhombus bisect each other at right angles.',
         sol='The diagonals cut each other in half at right angles, giving four right triangles with legs 8 cm and 15 cm. Each side is √(64 + 225) = √289 = 17 cm. Perimeter = 4 × 17 = 68 cm.'),
    dict(ch='5', scen='girl 1.5 m tall standing 4 m from a 6 m lamp post · shadow',
         fig=drawing(190, 165, lamp()),
         stem='Riya, 1.5 m tall, stands 4 m from the foot of a 6 m lamp post, as shown. How long is her shadow?',
         opts=['4/3 m', '1 m', '3/4 m', '16/3 m'],
         hint='The girl and the lamp post make two similar right triangles that share the tip of the shadow.',
         sol='Let the shadow be s m. The small triangle (height 1.5, base s) is similar to the large one (height 6, base 4 + s). So 1.5/s = 6/(4 + s), giving 1.5(4 + s) = 6s, 6 + 1.5s = 6s, 4.5s = 6 and s = 4/3 m.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='closed cylinder radius 7 height 10 · total surface area',
         stem='A closed cylindrical tin has radius 7 cm and height 10 cm. What is its total surface area? (Take π = 22/7.)',
         opts=['748 cm²', '440 cm²', '594 cm²', '1,540 cm²'],
         hint='Total surface = curved surface + top + bottom = 2πr(h + r).',
         sol='Curved surface = 2πrh = 2 × 22/7 × 7 × 10 = 440 cm². Each circular end = πr² = 154 cm². Total = 440 + 2 × 154 = 748 cm². (594 counts only one end.)'),
    dict(ch='6', scen='cone radius 7 height 24 · curved surface area via slant height',
         stem='A cone has base radius 7 cm and height 24 cm. What is its curved surface area? (Take π = 22/7.)',
         opts=['550 cm²', '528 cm²', '704 cm²', '1,232 cm²'],
         hint='The curved surface uses the slant height l, found from r and h.',
         sol='Slant height l = √(7² + 24²) = √625 = 25 cm. Curved surface = πrl = 22/7 × 7 × 25 = 550 cm². (528 wrongly uses the height; 704 adds the base.)'),
    dict(ch='6', scen='tank 2 m by 1.5 m by 1 m filled at 50 litres a minute',
         stem='A tank 2 m long, 1.5 m wide and 1 m deep is filled by a pipe that delivers 50 litres every minute. How long does it take to fill the empty tank?',
         opts=['1 hour', '6 hours', '10 minutes', '6 minutes'],
         hint='1 m³ = 1,000 litres.',
         sol='Volume = 2 × 1.5 × 1 = 3 m³ = 3,000 litres. Time = 3,000 ÷ 50 = 60 minutes = 1 hour.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='histogram of test marks · percentage scoring 50 or more',
         fig=drawing(300, 200, hist([20, 30, 40, 50, 60, 70], [5, 7, 12, 10, 6], 12, 2, 'Marks')),
         stem='The histogram shows the marks of a class in a test (each class includes its lower mark, not its upper mark). What percentage of the class scored 50 marks or more?',
         opts=['40%', '16%', '70%', '25%'],
         hint='Add all the bars for the total, then add the bars from 50 onwards.',
         sol='Total = 5 + 7 + 12 + 10 + 6 = 40 students. Scoring 50 or more: 10 + 6 = 16. 16 ÷ 40 = 40%.'),
    dict(ch='8', scen='mean of 6 numbers 15 · removing different numbers gives means 14 and 16',
         stem='The mean of six numbers is 15. If one number is removed, the mean of the rest is 14. If, instead, a different number is removed, the mean of the rest is 16. What is the difference between these two numbers?',
         opts=['10', '2', '30', '5'],
         hint='Work with totals, not means.',
         sol='Total of six = 90. Removing the first leaves 5 × 14 = 70, so it was 20. Removing the second leaves 5 × 16 = 80, so it was 10. Difference = 20 − 10 = 10.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='two articles sold at ₹990 each at 10 percent profit and 10 percent loss',
         stem='Gopal sells two chairs for ₹990 each. On one he gains 10% and on the other he loses 10%. What is his overall result?',
         opts=['1% loss', 'No profit no loss', '1% profit', '2% loss'],
         hint='Find each cost price first. They are not equal.',
         sol='Cost of the first: 990 ÷ 1.1 = ₹900. Cost of the second: 990 ÷ 0.9 = ₹1,100. Total cost ₹2,000, total sale ₹1,980. Loss ₹20, which is 20/2,000 = 1%.'),
    dict(ch='9', scen='₹12,000 split between 8 and 10 percent simple interest earning ₹1,060',
         stem='Meera invests ₹12,000, part at 8% and the rest at 10% simple interest a year. Her total interest for one year is ₹1,060. How much did she invest at 10%?',
         opts=['₹5,000', '₹7,000', '₹6,000', '₹4,000'],
         hint='If all ₹12,000 were at 8%, the interest would be ₹960.',
         sol='At 8% on everything, interest would be ₹960. The extra ₹100 comes from the part at 10%, which earns 2% more. 2% of that part = ₹100, so the part is ₹5,000. Check: 8% of 7,000 + 10% of 5,000 = 560 + 500 = ₹1,060.'),
    dict(ch='9', scen='marked 40 percent above cost with 15 percent discount · profit percent',
         stem='A shopkeeper marks his goods 40% above cost price and then gives a discount of 15% on the marked price. What is his profit percent?',
         opts=['19%', '25%', '21%', '15%'],
         hint='Take the cost price as ₹100.',
         sol='Cost ₹100, marked ₹140. Discount 15% of 140 = ₹21, so he sells for ₹119. Profit = 19%.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='AB plus BA is 121 and AB minus BA is 27',
         stem='AB and BA are two-digit numbers made from digits A and B. AB + BA = 121 and AB − BA = 27. What is AB?',
         opts=['74', '47', '83', '65'],
         hint='AB + BA = 11(A + B) and AB − BA = 9(A − B).',
         sol='11(A + B) = 121 gives A + B = 11. 9(A − B) = 27 gives A − B = 3. So A = 7 and B = 4, and AB = 74. Check: 74 + 47 = 121 and 74 − 47 = 27.'),
    dict(ch='10', scen='three-digit numbers with digit sum 5',
         stem='How many three-digit numbers have digits that add up to 5?',
         opts=['15', '21', '10', '12'],
         hint='Count by the hundreds digit, which can be 1 to 5.',
         sol='Hundreds digit 1: tens + ones = 4, 5 ways. Digit 2: sum 3, 4 ways. Digit 3: 3 ways. Digit 4: 2 ways. Digit 5: 1 way. Total 5 + 4 + 3 + 2 + 1 = 15.'),
    dict(ch='10', scen='largest number dividing n cubed minus n for every n at least 2',
         stem='For every whole number n ≥ 2, the number n³ − n is divisible by a certain largest whole number. What is it?',
         opts=['6', '3', '2', '12'],
         hint='Factorise n³ − n into three consecutive numbers.',
         sol='n³ − n = (n − 1)n(n + 1), three consecutive numbers. One is even and one is a multiple of 3, so the product is always divisible by 6. For n = 2 it equals 6, so no larger number works for every n.'),
    dict(ch='10', scen='Sierpinski triangle · fraction still shaded after step 4',
         fig=drawing(330, 110, sierp_steps()),
         stem='At each step, every shaded triangle is split into four equal triangles and the middle one is removed. Steps 0, 1 and 2 are shown. What fraction of the original triangle is still shaded after step 4?',
         opts=['81/256', '3/16', '27/64', '1/4'],
         hint='Each step keeps 3 of every 4 equal parts.',
         sol='Each step keeps 3/4 of the shaded area. After 4 steps: (3/4)⁴ = 81/256. (27/64 is the fraction after step 3.)'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='three consecutive odd numbers summing to 147 · product of the outer two',
         stem='Three consecutive odd numbers add up to 147. Using an identity rather than long multiplication, find the product of the smallest and the largest.',
         opts=['2,397', '2,401', '2,499', '2,352'],
         hint='The middle number is 147 ÷ 3. The outer numbers are 2 less and 2 more.',
         sol='The middle number is 49, so the numbers are 47, 49 and 51. 47 × 51 = (49 − 2)(49 + 2) = 49² − 4 = 2,401 − 4 = 2,397.'),
    dict(ch='5+10', scen='right triangles with whole-number sides and hypotenuse 25',
         stem='How many different right-angled triangles have whole-number sides and a hypotenuse of exactly 25 cm?',
         opts=['2', '1', '3', '4'],
         hint='Look for whole numbers a < b with a² + b² = 625.',
         sol='Try a from 1 to 17: 625 − a² is a perfect square only for a = 7 (576 = 24²) and a = 15 (400 = 20²). So the triangles are 7, 24, 25 and 15, 20, 25: 2 triangles.'),
    dict(ch='4+5', scen='rectangle with length 7 more than width and perimeter 34 · diagonal',
         stem='The length of a rectangle is 7 cm more than its width, and its perimeter is 34 cm. How long is a diagonal?',
         opts=['13 cm', '17 cm', '12 cm', '15 cm'],
         hint='Length + width = 17. Find the sides, then use Pythagoras.',
         sol='Width w, length w + 7, so 2(2w + 7) = 34, 2w + 7 = 17 and w = 5. The sides are 5 cm and 12 cm, and the diagonal is √(25 + 144) = √169 = 13 cm.'),
    dict(ch='3+9', scen='simple interest 3 years at 8 percent exceeds 2 years at 9 percent by ₹1,200',
         stem='The simple interest on a sum for 3 years at 8% a year is ₹1,200 more than the simple interest on the same sum for 2 years at 9% a year. What is the sum?',
         opts=['₹20,000', '₹12,000', '₹15,000', '₹24,000'],
         hint='Compare the total percentages: 3 × 8% and 2 × 9%.',
         sol='3 years at 8% gives 24% of the sum; 2 years at 9% gives 18%. The difference, 6% of the sum, is ₹1,200. So the sum = 1,200 × 100 ÷ 6 = ₹20,000.'),
    dict(ch='6+9', scen='cylindrical tank radius 1.4 m height 2 m · cost of water at 5 paise a litre',
         stem='A cylindrical tank has radius 1.4 m and height 2 m. Water costs 5 paise per litre. What does it cost to fill the empty tank? (Take π = 22/7.)',
         opts=['₹616', '₹6,160', '₹308', '₹1,232'],
         hint='Volume = πr²h; 1 m³ = 1,000 litres; 100 paise = ₹1.',
         sol='Volume = 22/7 × 1.4 × 1.4 × 2 = 12.32 m³ = 12,320 litres. Cost = 12,320 × 5 paise = 61,600 paise = ₹616.'),
]
