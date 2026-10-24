"""House-rule checks for AMO Level-2 question files (syllabus v5.9, Language & Culture, Visual Standards).

check_paper() stops the build on any hard failure. check_all() also checks rules that span papers
(every scenario used once across the whole set of papers)."""
import re

GIRLS = set('''Anita Meera Priya Isha Diya Kavya Riya Anaya Tara Sana Pooja Asha Nisha Gauri Leela Siya Myra Ira
Tanvi Avni Navya Mahi Jiya Kiara Neha Ritu Sneha Aditi Pari Ruhi Vani Juhi Lata Rani Uma Esha Ananya Shreya
Trisha Sita Bela Charu Disha Gita Hema Indu Jaya Komal Lavanya Madhu Nandini Pallavi Radha Shalini Tulsi Urvi
Vidya Yamini Aarti Bhavna Chhaya Deepa Ekta Falguni Garima Harini Ishita Janvi Kirti Mansi Naina Ojasvi Prachi
Rekha Sakshi Meena Kusum Leena Shruti Sapna Sunita Neelam Hema Tanya Upasana Vaishnavi Anjali Rupa Manju Seema Suhani Amrita Mitali Payal Rashmi Devika Ishani Mohini Charvi Nitya Kriti Swati Rhea Parul Vrinda'''.split())
BOYS = set('''Raj Arjun Kabir Rohan Aarav Vivaan Ishaan Dev Neel Kunal Yash Om Manav Varun Aditya Harsh Parth Samar
Advik Krish Vihaan Reyansh Ravi Amit Nikhil Sahil Tarun Ved Ayaan Dhruv Rahul Sanjay Vikram Mohan Gopal Hari Jay
Lakshya Mihir Nakul Pranav Rudra Shaurya Tejas Uday Vansh Yuvraj Aryan Bhavin Chirag Darsh Eshan Gautam Gaurav Raju Hitesh
Jatin Kartik Abhay Bharat Deepak Girish Hemant Ishwar Jai Kishore Lalit Madhav Naveen Omkar Prakash Rakesh Suresh
Tushar Umesh Vinay Mohit Ojas Rohit Lalit Raghav Hari Vivek Mukesh Sohan Akash Ankit Rishi Sameer Vijay Atul Mayank Pratik Siddharth Anand Kush Luv Ajay Karan Arnav Kiran Sunil Manoj Ritesh Vedant Aakash Ishan Pankaj Nitin Sachin'''.split())
NAMES = GIRLS | BOYS

# Capitalised words that may start a sentence or name a thing, not a person.
NOT_NAMES = set('''A An The How What Which Who Whom Whose Where When Why If In On At Of To For From By With Each Every
Some Many Most All Both Then There This That These Those Her His Their He She They It Its One Two Three Four Five Six
Seven Eight Nine Ten Look Count Find Start Read Write Fill Put Use Make Share Draw Fold Cut Move Join Add Take Give
Is Are Was Were Do Does Did Can Could Will Would Should Section Part Star Monday Tuesday Wednesday Thursday Friday
Saturday Sunday January February March April May June July August September October November December Mon Tue
Wed Thu Fri Sat Sun Picture Group Box Card Row Column Shape Figure Figures Tower Bag Basket Plate Jar Purse Team
Path Line Lines Bus Train Room Floor Stop Gate Pot Pots Q P R S T X Y Z B C D E F G H K L M N O U V W I II
Not No Yes Only Also Next Last First Second Third After Before Now Today Tomorrow Yesterday Hint Every At Here
Sticks Coins Notes Pages Page Book Books Tray Trays Step Steps Number Numbers Tens Ones Ten Ones Rows Rod Rods
Clock Year Week Month Months Days Day Help Lift Ticket Tickets Seat Seats Locker Lockers Bead Beads Ring Rings
Each Either Neither Round Square Circle Triangle Rectangle Children Class Teacher School Library Park Garden
Market Shop Indian India Sundays Mondays Saturdays Fridays Tuesdays Wednesdays Thursdays Roman Coach Domino Point Grandma Grandpa Mother Father Aunt Uncle Sister Brother Mummy Papa Dadi Nani Nana Dada Mr Mrs Ms'''.split())

STARTERS = set('''Later Into Ball Bat Cap Lunch Both Each Every Some Pages Houses Lockers Raffle Eggs Dots Shapes Hens Coins Coins Numbers Months Days
Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Going Look Count Find Which What How Who Where When Whose
The A An In On At If Then There This That These Those She He They It Its Her His My I Now Today Tomorrow Yesterday
School Points Part Players Rows Row Lines Each Every Both Neither Use Using Write Put Thirteen Eleven Twelve Fourteen
Without Sort Think Counting Point Ten Taking After Before Only Once Twice Cone Cylinder Sphere Cube Half Quarter Clock Rows Piece Pictures Shirt Exactly Dates Choose Putting You Together Pencil Eraser Sharpener Noon Midnight Morning Evening Night Hall Triangular Square Rectangular Cuboid Pyramid Prism'''.split())
WORD_CAP = 25          # Language & Culture rule 8: max 25 words per sentence for C1-3, 35 for C4-6
ADD_CAP = 24           # Computational ceiling: C1 sums within 20 (+20% allowed for Section II); C2 sums within 999
CAPS = {1: 24, 2: 999, 3: 10000, 4: 100000}


def set_class(cls):
    global ADD_CAP, WORD_CAP
    ADD_CAP = CAPS.get(cls, 10 ** 9)
    WORD_CAP = 25 if cls <= 3 else 35


def sentences(text):
    return [s for s in re.split(r'(?<=[.?!])\s+', text.strip()) if s]


def names_in(text):
    """Capitalised words that look like personal names. A capitalised word at the start of a
    sentence counts only if it is a known name; elsewhere any capitalised word not in NOT_NAMES counts."""
    out = []
    for sent in sentences(text):
        words = re.findall(r"[A-Za-z']+", sent)
        for k, w in enumerate(words):
            w = w.split("'")[0]
            if not w[:1].isupper() or not w[1:].islower():
                continue
            if w in NAMES or (k > 0 and w not in NOT_NAMES):
                out.append(w)
    return out


def check_paper(pno, qs, parts, stars, strict=True):
    errs, warns = [], []
    want = [c for c, _, n in parts for _ in range(n)] + list(stars)
    if len(qs) != len(want):
        errs.append(f'P{pno}: {len(qs)} questions, expected {len(want)}')
    girls = boys = 0
    for i, q in enumerate(qs, 1):
        tag = f'P{pno} Q{i}'
        for k in ('ch', 'stem', 'opts', 'hint', 'sol', 'scen'):
            if not q.get(k):
                errs.append(f'{tag}: missing {k}')
        if i <= len(want) and q.get('ch') != want[i - 1]:
            errs.append(f'{tag}: chapter {q.get("ch")} but blueprint wants {want[i - 1]}')
        opts = q.get('opts', [])
        if len(opts) != 4 or len(set(map(str, opts))) != 4:
            errs.append(f'{tag}: needs 4 different options: {opts}')
        if q.get('fixed') and q.get('ans') not in (0, 1, 2, 3):
            errs.append(f'{tag}: fixed order needs ans index')
        text = ' '.join([q.get('stem', '')] + [str(o) for o in opts])
        if re.search(r'\bRs\.?\b', text + q.get('sol', '')):
            errs.append(f'{tag}: write ₹, not Rs.')
        for s in sentences(q.get('stem', '')):
            n = len(s.split())
            if n > WORD_CAP:
                errs.append(f'{tag}: sentence has {n} words (max {WORD_CAP}): {s}')
        if re.match(r'^\d', q.get('stem', '')):
            warns.append(f'{tag}: stem starts with a numeral')
        for t in [q.get('stem', '')] + [str(o) for o in opts]:
            for sent in sentences(t):
                w = (re.findall(r"[A-Za-z]+", sent) or [''])[0]
                if w[:1].isupper() and w[1:].islower() and w not in NAMES and w not in NOT_NAMES and w not in STARTERS:
                    warns.append(f'{tag}: sentence starts with "{w}" - if this is a name, use one from the Indian-names list')
        for nm in [n for t in [q.get('stem', '')] + [str(o) for o in opts] for n in names_in(t)]:
            if nm in GIRLS:
                girls += 1
            elif nm in BOYS:
                boys += 1
            else:
                errs.append(f'{tag}: "{nm}" is not in the Indian-names list (add it to checks.py if it is a name, or to NOT_NAMES if not)')
        for a, b in re.findall(r'(\d+)\s*\+\s*(\d+)', q.get('sol', '')):
            if int(a) + int(b) > ADD_CAP and not q.get('place_value_ok'):
                warns.append(f'{tag}: solution adds {a} + {b} (> {ADD_CAP}); check it is place-value counting, not an addition fact')
    if girls and boys and (max(girls, boys) > 2 * min(girls, boys) + 2):
        warns.append(f'P{pno}: name balance girls {girls} vs boys {boys}')
    for w in warns:
        print('  warn:', w)
    if errs and strict:
        raise SystemExit('\n'.join(errs))
    return errs, warns


def check_all(papers):
    """papers: {pno: QUESTIONS}. Every scenario key must be used exactly once across all papers."""
    seen, errs = {}, []
    for p, qs in papers.items():
        for i, q in enumerate(qs, 1):
            k = re.sub(r'\s+', ' ', q['scen'].strip().lower())
            if k in seen:
                errs.append(f'scenario "{k}" used in P{seen[k][0]} Q{seen[k][1]} and P{p} Q{i}')
            seen[k] = (p, i)
    stems = {}
    for p, qs in papers.items():
        for i, q in enumerate(qs, 1):
            s = re.sub(r'\W+', ' ', q['stem'].lower()).strip()
            if s in stems:
                errs.append(f'same stem in P{stems[s][0]} Q{stems[s][1]} and P{p} Q{i}')
            stems[s] = (p, i)
    return errs
