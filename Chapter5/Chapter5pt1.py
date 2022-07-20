# squares.py
def square1(n):
    return n ** 2   # slightly slower
def square2(n):
    return n * n    # slightly faster

# decorate.sort.undecorate.py
students = [
    dict(id=0, 
    credits=dict(math=9, physics=6, history=7)), 
    dict(id=1, 
    credits=dict(math=6, physics=7, latin=10)),
    dict(id=2,
    credits=dict(history=8, physics=9, chemistry=10)), 
    dict(id=3,
    credits=dict(math=5, physics=5, geography=7)),
]
def decorate(student):
    # create a 2-tuple (sum of credits, student) from student dict
    (sum(student['credits'].values()), student)
    return

# def undecorate(decorated_student):
    # discard sum of credits, return  original student dict
#    return decorated_student[1]
#students = sorted(map(decorate, students), reverse=True)
#students = list(map(undecorate, students))
#print(students)
#Error occurs^^^

# maxims.py     for the command line
# a = [5, 9, 2, 4, 7]
# b = [3, 7, 1, 9, 2]
# c = [6, 8, 0, 5, 3]
# maxs = map(lambda n : max(*n), zip(a, b, c))
# print(list(maxs))   # [6, 9, 2, 9, 7]

# squares.map.py
# squares = []
# for n in range(10):
#   squares.append(n ** 2)

# squares   
# Returns: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# The better way 
# squares = map(lambda n: n**2, range(10))
# list(squares)
# Returns: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# squares.comprehension.py
# [n ** 2 for n in range(10)]
# Returns: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# even.squares.py
# useing map and filter
sq1 = list(
    map(lambda n: n ** 2, filter(lambda n: not n % 2, range(10)))
)

# equivalent, but using list comprehensions
sq2 = [n ** 2 for n in range(10) if not n % 2]
print(sq1, sq1 == sq2)  # prints: [0, 4, 16, 36, 64] True

# pairs.for.loop.py
items = 'ABCD'
pairs = []
for a in range(len(items)):
    for b in range(a, len(items)):
        pairs.append((items[a], items[b]))
print(pairs)

# pairs.list.comprehension.py
items = 'ABCD'
pairs = [(items[a], items[b])for a in range(len(items))for b in range(a, len(items))]
print(pairs)

# pythagorean.triple.py
from math import sqrt
# this will generate all possible pairs
mx = 10
triples = [(a, b, sqrt(a**2 + b**2))for a in range(1, mx) for b in range(a, mx)]
# this will filter out all non Triples
triples = list(
    filter(lambda triple:
    triple[2].is_integer(), triples))
print(triples)  # prints: [(3, 4, 5.0), (6, 8, 10.0)]

# pythagorean.triple.int.py
from math import sqrt
mx = 10
triples = [(a, b, sqrt(a**2 + b**2))
    for a in range(1, mx) for b in range(a, mx)]
triples = filter(lambda triple: triple[2].is_integer(), triples)  # this will make the third number in the tuples integer
triples = list(
    map(lambda triple: triple[:2] + (int(triple[2]), ), triples))
print(triples)  # prints: [(3, 4, 5), (6, 8, 10)]

# pythagorean.triple.comprehension.py
from math import sqrt
# this step is the same as before
mx = 10 
triples = [(a, b, sqrt(a**2 + b**2))
    for a in range(1, mx) for b in range(a, mx)]
# here we combine filter an map in one CLEAN list comprehension
triples = [(a, b, int(c)) for a, b, c in triples if c.is_integer()]
print(triples) # prints the same as before

# pythagorean.triple.walrus.py
from math import sqrt
# this step is the same as before
mx = 100
3 # We can combine generating and filtering in one list comprehension
triples = [(a, b, int(c))
    for a in range(1, mx) for b in range(a, mx)
    if (c := sqrt(a**2 + b**2)).is_integer()]
print(triples)   # prints the same again

# dictionary.comprehensions.py
from string import ascii_lowercase
lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}
print(lettermap)

# Same thing Differently
# lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))

# dictionary.comprehensions.duplicates.py
word = 'Hello'
swaps = {c: c.swapcase() for c in word}
print(swaps)  # prints a long string

# dictionary.comprehensions.positionns.py
word = 'Hello'
positions = {c: k for k, c in enumerate(word)}
print(positions) # prints: {'H':0, 'e': 1, 'l': 3, 'o': 4}

# set.comprehensions.py
word = 'Hello'
letters1 = {c for c in word}
letters2 = set(c for c in word)
print(letters1) # prints: {'H', 'o', 'e', 'l'}
print(letters1 == letters2)  # prints: True