"""Apply Class 1 review fixes to the v2 DOCX files and write v3 copies.

Every replacement matches a whole <w:t> text run exactly and must match once
(or the stated count), otherwise the script stops.
"""
import html, re, shutil, sys, zipfile

SRC = sys.argv[1]   # folder with AMO_C1_L1_PracticePaperN_v2.docx
OUT = sys.argv[2]   # output folder for v3 docx

COVER = [
    ("Look at the picture or read the question carefully. Then mark your answer on the answer sheet at the end.",
     "Read each question and look at its picture carefully. Then mark your answer on the answer sheet at the end."),
    ("The answer sheet and the answer key with solutions are at the end. Detach them before the child begins.",
     "The answer sheet and the answer key with solutions are at the end. Give the child the answer sheet. Remove the answer key and solutions before the child begins."),
]
DROP_PARA = ["All figures are not necessarily drawn to scale unless stated."]

# (old, new) for whole text runs. ("@after", anchor, old, new) replaces the
# first run equal to old that follows the anchor run. ("@before", ...) uses the
# nearest run before the anchor.
FIX = {
1: [
 ("Look at the four pictures. Which picture has the fewest balloons?",
  "Look at the four pictures. Which picture has the smallest number of balloons?"),
 ("Shreya counts in tens: 10, 20, 30, and so on. 70 is 7 tens. Which number does she say just after 70?",
  "Shreya counts in tens: 10, 20, 30, and so on. Which number does she say just after 70?"),
 ("Look at the books. Two books swap places. Then the numbers are in order, smallest first. Which two books swap?",
  "Look at the books. Which two books should swap places so that the numbers are in order, smallest first?"),
 ("6 children are in the swimming pool. Then 8 more children jump in. How many children are in the pool now?",
  "There are 6 children in the swimming pool. Then 8 more children jump in. How many children are in the pool now?"),
 ("18 children go on a bicycle trip. 5 of them stop to rest. How many children are still riding?",
  "There are 18 children on a bicycle trip. Then 5 of them stop to rest. How many children are still riding?"),
 ("A rainwater tank holds 20 buckets of water. 6 buckets are used for the garden. 5 buckets are used for washing. How many buckets of water are left?",
  "A rainwater tank holds 20 buckets of water. Amma uses 6 buckets for the garden and 5 buckets for washing. How many buckets of water are left in the tank?"),
 ("Star, balloon, car, fish: these four pictures repeat again and again. Which one goes in the box?",
  "Look at the pictures. Star, balloon, car and fish repeat again and again in the same order. Which picture goes in the box?"),
 ("Three of these numbers come one after the other. Which is the odd one out?",
  "Three of these numbers come one after the other. Which number does NOT belong with them?"),
 ("The shapes on the left make a pattern. A grey card hides one. The right side is the left side folded over. Which shape goes in the box?",
  "The shapes on the left of the red line make a pattern. A grey card hides one shape. If you fold the paper on the red line, each shape on the right lands on a matching shape on the left. Which shape goes in the box?"),
 ("A water tank is cleaned in the starred months on the chart. The gap is always the same. In which month was it cleaned just before April?",
  "A water tank is cleaned in the starred months on the chart. The gap between cleanings is always the same. After October, in which month will the tank be cleaned next?"),
 ("From April to July is 3 months, and from July to October is 3 months. Three months before April is January.",
  "From April to July is 3 months, and from July to October is 3 months. Three months after October is January."),
 ("From Monday to Saturday, Samar saves a ₹10 note each day. He also saves a ₹2 coin on Wednesday and one on Friday. How much does he save?",
  "From Monday to Saturday, Samar saves a ₹10 note each day. He also saves a ₹2 coin on Wednesday and another ₹2 coin on Friday. How much money does he save in all?"),
 ("In Picture A the dotted line goes down the middle, so the two parts have the same size and shape. In the other pictures one part is bigger.",
  "In Picture A the dotted line goes down the middle, so the two parts have the same size and shape. In the other pictures the parts do not match."),
 ("@addrun", "September, October and November come one after another. In each other list two months are swapped.",
  "(B) ", "Sep, Oct, Nov"),
],
2: [
 ("A toy shop packs balls in bags of 10. Which number of balls leaves no ball loose?",
  "A toy shop packs balls in bags of 10. Which number of balls fills the bags with no balls left over?"),
 ("Which of these number names goes with the right number?",
  "Which number name matches its number correctly?"),
 ("Look at the picture. The desks in a row are numbered in order. Which number is hidden?",
  "Look at the number cards. They are in order. Which number is hidden?"),
 ("Look at the plates of mushrooms. Which picture shows 4 plates of 5?",
  "Look at the plates of mushrooms. Which picture shows 4 plates with 5 mushrooms on each plate?"),
 ("9 + 5 = 14 is true. Each answer choice uses the same three numbers. Which of these is also true?",
  "We know that 9 + 5 = 14. Which of these number sentences is also true?"),
 ("A shape card has fallen on its side, as in the picture. What is the name of the shape?",
  "A shape card is turned, as in the picture. What is the name of the shape?"),
 ("Look at the picture. Two kinds of shapes are equal in number. Which two?",
  "Look at the picture. Count each kind of shape. Which two kinds of shapes have the same count?"),
 ("Which of these months comes earliest in the year?",
  "Which of these months comes first in the year?"),
 ("Look at the four rows. Which picture repeats circle, triangle, triangle?",
  "Look at the four rows. Which row repeats circle, triangle, triangle?"),
 ("@after", "Look at the four rows. Which row repeats circle, triangle, triangle?", "Picture A", "Row A"),
 ("@after", "Look at the four rows. Which row repeats circle, triangle, triangle?", "Picture B", "Row B"),
 ("@after", "Look at the four rows. Which row repeats circle, triangle, triangle?", "Picture C", "Row C"),
 ("@after", "Look at the four rows. Which row repeats circle, triangle, triangle?", "Picture D", "Row D"),
 ("Look at the number pattern. The jumps grow in the same way each time. How many tens and ones does the next number have?",
  "Look at the number pattern. Each jump is 1 more than the jump before. How many tens and ones does the next number have?"),
 ("Yuvan counts by tens: 10, 20, 30, and so on up to 100. How many of these numbers are the value of an Indian note?",
  "Yuvan counts by tens: 10, 20, 30, and so on up to 100. For how many of these numbers is there an Indian rupee note?"),
 ("Look at the picture. Pihu pays using only these two kinds of money. Which of these amounts needs the fewest notes and coins?",
  "Look at the picture. Pihu pays the exact amount using only these two kinds of money. Which amount needs the smallest number of notes and coins in all?"),
 ("A triangle needs 3 sticks and a square needs 4. 3 + 3 + 4 = 10 sticks. The others need 11, 9 and 8 sticks.",
  "A triangle needs 3 sticks and a square needs 4. 3 + 3 + 4 = 10 sticks. 3 triangles need 9 sticks, 2 squares need 8, and 1 triangle and 2 squares need 11."),
 ("@addrun", "A triangle needs 3 sticks and a square needs 4. 3 + 3 + 4 = 10 sticks. 3 triangles need 9 sticks, 2 squares need 8, and 1 triangle and 2 squares need 11.",
  "(C) ", "2 triangles and 1 square"),
],
3: [
 ("1 more than 79 is ___.", "The number that is 1 more than 79 is ___."),
 ("6 tens and ___ ones make 67.", "The number 67 is 6 tens and ___ ones."),
 ("Each box shows bundles of ten sticks and some loose sticks. Which box shows the greatest number?",
  "Each box shows bundles of ten sticks. Some boxes also have loose sticks. Which box shows the greatest number?"),
 ("Look at the dominoes from a board game. Which domino has 11 dots in all?",
  "Look at the dominoes. Which domino has 11 dots in all?"),
 ("The hops on the number line show a take-away sum. Which number fills the blank?",
  "The hops on the number line show a take-away. Which number fills the blank?"),
 ("Which take-away sum gives 9?", "Which take-away gives 9?"),
 ("Some mangoes hang on a tree. 5 mangoes fall down. Now 11 mangoes are on the tree. How many mangoes were on the tree at first?",
  "Some mangoes hang on a tree. Then 5 mangoes fall down. Now 11 mangoes are on the tree. How many mangoes were on the tree at first?"),
 ("Look at the number cards. Both sides of = must give the same answer. Which number goes in the box marked with a question mark?",
  "Look at the number cards. The two sides of the = sign must be equal. Which number goes in the box with the question mark?"),
 ("Half of a shape is drawn beside a fold line. The other half is the same. Which picture shows the whole shape?",
  "Half of a shape is drawn next to a fold line. The other half is the same, on the other side of the fold line. Which picture shows the whole shape?"),
 ("This picture of a museum is made of shapes. Which shape is NOT in the picture?",
  "This picture of a house is made of shapes. Which shape is NOT in the picture?"),
 ("Three of the four shapes are alike: each has 3 corners. Which picture is the odd one out?",
  "Three of the four shapes are alike. Each of them has 3 corners. Which picture does NOT belong with them?"),
 ("It goes on in the same way. Which of these numbers comes later in the pattern?",
  "It goes on in the same way. Which of these numbers will also be in the pattern?"),
 ("Look at the tens in these numbers. Three of them have the same number of tens. Which number is the odd one out?",
  "Look at the tens in these numbers. Three of them have the same number of tens. Which number does NOT belong with them?"),
 ("All 4 sides of a square have the same length. Each drawn side is 2 dots long, so the last corner is 2 dots above the end of the bottom side. That is the dot marked R.",
  "All 4 sides of a square have the same length. Each drawn side goes 2 spaces from dot to dot. So the last corner is 2 spaces straight up from the right end of the bottom side. That is the dot marked R."),
 ("Our coins are ₹1, ₹2, ₹5 and ₹10. The coin between ₹2 and ₹10 is the ₹5 coin.",
  "Our coins are ₹1, ₹2, ₹5, ₹10 and ₹20. The coin between ₹2 and ₹10 is the ₹5 coin."),
],
4: [
 ("Look at the picture. The ducks walk in pairs. How many ducks are there?",
  "Look at the picture. How many ducks are there?"),
 ("Look at the numbers worn by four children. They stand in an assembly row from the greatest number to the smallest. Which row is correct?",
  "Four children wear these number cards. They stand in a row from the greatest number to the smallest. Which row is correct?"),
 ("Look at the two digit cards of Kiara. She uses both cards to make a number. What is the greatest number she can make?",
  "Kiara has two digit cards. She uses both cards to make a number. What is the greatest number she can make?"),
 ("Look at the plates of cherries. Komal wants 5 cherries on every plate. How many more cherries does she need?",
  "Look at the plates. Each picture shows a bunch of cherries. Komal wants 5 bunches on every plate. How many more bunches does she need?"),
 ("The last plate has 3 cherries. 3 and 2 more make 5, so she needs 2 more cherries.",
  "The first two plates have 5 bunches each. The last plate has 3 bunches. 3 and 2 more make 5, so she needs 2 more bunches."),
 ("A plant nursery has 12 saplings. 7 more saplings arrive. Then 5 saplings are sold. How many saplings does the nursery have now?",
  "A plant shop has 12 small plants. Then 7 more plants arrive. After that, 5 plants are sold. How many plants does the shop have now?"),
 ("12 + 7 = 19. Then 19 − 5 = 14. The nursery has 14 saplings.",
  "12 + 7 = 19. Then 19 − 5 = 14. The shop has 14 plants."),
 ("Chitra gives a sapling plant food on a Tuesday. She gives it plant food again 7 days later. On which day is that?",
  "Chitra feeds her small plant on a Tuesday. She feeds it again 7 days later. On which day is that?"),
 ("Look at the numbers of the ferry boats on a river. They make a pattern. Which number is on the next boat?",
  "Look at the numbers on the cards. They make a pattern. Which number comes next?"),
 ("Rosa plays badminton on Monday, Tuesday, Thursday and Sunday. The gaps grow: 1 day, 2 days, 3 days. On which day does she play next?",
  "Rosa plays badminton on Monday, Tuesday, Thursday and Sunday. She plays 1 day later, then 2 days later, then 3 days later. Each time she waits one more day. On which day does she play next?"),
],
5: [
 ("How many numbers are greater than 37 and less than 42?",
  "How many numbers come between 37 and 42?"),
 ("Look at the owls. They sit on a branch. All of them fly away. How many owls are left on the branch?",
  "Look at the owls in the picture. All of them fly away. How many owls are left?"),
 ("7 planes are at the airport. 5 more planes land. How many planes are at the airport now?",
  "There are 7 planes at the airport. Then 5 more planes land. How many planes are at the airport now?"),
 ("A tea stall has 15 clean cups. 6 cups get used. How many clean cups are left?",
  "A tea stall has 15 clean cups. People use 6 of the cups. How many clean cups are left?"),
 ("18 children are on the playground swings and slides. Some go home, and 11 children are still playing. How many children went home?",
  "There are 18 children in the playground. Some children go home. Now 11 children are still playing. How many children went home?"),
 ("Look at the plates of watermelon slices. One more plate with the same number of slices is added. How many slices are there then?",
  "Look at the plates of watermelon slices. Mum puts one more plate with the same number of slices on the table. How many slices are there now?"),
 ("I am round. I have no corners at all. Which shape am I?",
  "I have no corners and no straight sides. Which shape am I?"),
 ("Look at the four shapes. Each has a dotted line. In which picture are the two sides of the dotted line NOT the same?",
  "Look at the four shapes. Each has a dotted line. In which picture does the dotted line NOT cut the shape into two halves that match?"),
 ("Look at the coins in Pari's purse. Our coins are ₹1, ₹2, ₹5 and ₹10. Which coin does Pari NOT have?",
  "Look at the coins in Pari's purse. Which of these coins does Pari NOT have?"),
 ("The number on the note Hana has is fifty. Which picture shows her note?",
  "Hana has a fifty-rupee note. Which picture shows her note?"),
 ("Look at the notes. Dhruv puts them in order from the least worth to the most. Which note comes second?",
  "Look at the notes. Dhruv puts them in order from the smallest amount to the biggest. Which note comes second?"),
 ("Look at the four number cards. Count the digits in each number. Which number is the odd one out?",
  "Look at the four number cards. Count the digits in each number. Which number has a different number of digits from the others?"),
],
}


def run(text):
    return '>' + html.escape(text, quote=False) + '</w:t>'


def runs_equal(x, text):
    pat = re.compile(r'<w:t(?: [^>]*)?' + re.escape(run(text)))
    return [m for m in pat.finditer(x)]


def sub_at(x, m, old, new):
    seg = m.group(0)
    return x[:m.start()] + seg.replace(run(old), run(new)) + x[m.end():]


PLAIN = '<w:r><w:rPr><w:b w:val="0"/><w:i w:val="0"/><w:sz w:val="20"/></w:rPr><w:t>{}</w:t></w:r>'


def apply(x, fix, paper):
    if fix[0] == "@addrun":
        # add a plain answer-text run after the bold letter run before the anchor
        _, anchor, letter, text = fix
        a = runs_equal(x, anchor)
        assert len(a) == 1, (paper, 'anchor', anchor, len(a))
        hits = [m for m in runs_equal(x, letter) if m.end() < a[0].start()]
        assert hits, (paper, 'no', letter, 'near', anchor)
        e = x.find('</w:r>', hits[-1].end()) + len('</w:r>')
        return x[:e] + PLAIN.format(html.escape(text, quote=False)) + x[e:]
    if fix[0] in ("@after", "@before"):
        mode, anchor, old, new = fix
        a = runs_equal(x, anchor)
        assert len(a) == 1, (paper, 'anchor', anchor, len(a))
        hits = runs_equal(x, old)
        if mode == "@after":
            hits = [m for m in hits if m.start() > a[0].end()][:1]
        else:
            hits = [m for m in hits if m.end() < a[0].start()][-1:]
        assert hits, (paper, 'no', old, 'near', anchor)
        return sub_at(x, hits[0], old, new)
    old, new = fix
    hits = runs_equal(x, old)
    assert len(hits) == 1, (paper, len(hits), old)
    return sub_at(x, hits[0], old, new)


def drop_para(x, text, paper):
    hits = runs_equal(x, text)
    assert len(hits) == 1, (paper, 'drop', text, len(hits))
    i = hits[0].start()
    s = max(x.rfind('<w:p>', 0, i), x.rfind('<w:p ', 0, i))
    e = x.find('</w:p>', i) + len('</w:p>')
    return x[:s] + x[e:]


for p in range(1, 6):
    src = f'{SRC}/AMO_C1_L1_PracticePaper{p}_v2.docx'
    dst = f'{OUT}/AMO_C1_L1_PracticePaper{p}_v3.docx'
    with zipfile.ZipFile(src) as z:
        x = z.read('word/document.xml').decode('utf-8')
        n = 0
        for f in COVER + FIX[p]:
            x = apply(x, f, p); n += 1
        for t in DROP_PARA:
            x = drop_para(x, t, p); n += 1
        with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as o:
            for item in z.infolist():
                data = x.encode('utf-8') if item.filename == 'word/document.xml' else z.read(item.filename)
                o.writestr(item, data)
    print(f'Paper {p}: {n} changes -> {dst}')
