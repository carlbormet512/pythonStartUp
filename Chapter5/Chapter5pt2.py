# first.n.squares.py
def get_squares(n): # classic function approach
    return [x ** 2 for x in range(n)]
print(get_squares(10))
def get_squares_gen(n):  # generator approach
    for x in range(n):
        yield x ** 2  # we yeild, we dont return
print(list(get_squares_gen(10)))

# first.n.squares.manual.py
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2
squares = get_squares_gen(4)  # this creates a generator object
print(squares)  # <generator object get_squares_gen at 0x10dd...>
print(next(squares))    # prints: 0
print(next(squares))    # prints: 1
print(next(squares))    # prints: 4
print(next(squares))    # prints: 9
# the following raises StopIteration, the generator is exausted,
# any further call to next will keep raising StopIteration
# print(next(squares))   Error occurs

# gen.yeild.return.py
def geometric_progression(a, q):
    k = 0
    while True:
        result = a * q**k 
        if result <= 100000:
            yield result
        else:
            return
        k += 1
for n in geometric_progression(2, 5):
    print(n)

# first.n.squares.manual.method.py
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2
squares = get_squares_gen(3)
print(squares.__next__())   # prints: 0
print(squares.__next__())   # prints: 1
print(squares.__next__())   # prints: 4
# the following raises StopIteration, the generator is exausted
# any further call will raise StopIteration
# print(squares.__next__())

# gen.send.preparation.py
def counter(start=0):
    n = start
    while True:
        yield n
        n += 1
c = counter()
print(next(c))
print(next(c))
print(next(c))

# gen.send.preparation.stop.py
stop = False
def counter(start=0):
    n = start
    while not stop:
        yield n
        n += 1
c = counter()
print(next(c))
print(next(c))
print(next(c))

# gen.send.py
def counter(start=0):
    n = start
    while True:
        result = yield n  # A
        print(type(result), result) # B
        if result == 'Q':
            break
        n += 1
c = counter()
print(next(c))          # C
print(c.send('Wow!'))   # D
print(next(c))          # E
#print(c.send('Q'))      # F
# the last one Raises the StopIteration

# gen.yield.for.py
def print_squares(start, end):
    for n in range(start, end):
        yield n ** 2
for n in print_squares(2, 5):
    print(n)

# gen.yield.from.py     better
def print_squares(start, end):
    yield from (n**2 for n in range(start, end))
for n in print_squares(2, 5):
    print(n)

# generator.expressions.py      # COMMAND LINE
# cubes = [k**3 for k in range(10)]  # regular list
# cubes
## [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
# type(cubes)
## <class 'list'>
# cubes_gen = (k**3 for k in rangw(10))  # create as a generator
# cubes_gen
## <generator object <genexpr> at ...>
# type(cubes_gen)
## <class 'generator'>
# list(cubes_gen)   # this will exhaust the generator
## [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
# list(cubes_gen)  # nothing more to give
## []

# gen.map.py
def adder(*n):
    return sum(n)
s1 = sum(map(adder, range(100), range(1, 101)))
s2 = sum(adder(*n) for n in zip(range(100), range(1, 101)))

# gen.filter.py
cubes = [x**3 for x in range(20)]
odd_cubes1 = filter(lambda cube: cube % 2, cubes)
odd_cubes2 = (cube for cube in cubes if cube % 2)

# gen.map.filter.py
N = 20
cubes1 = map(
    lambda n: (n, n**3), 
    filter(lambda n: n % 3 == 0 or n % 5 == 0, range(N))
)
cubes2 = (
    (n, n**3) for n in range(N) if n % 3 == 0 or n % 5 == 0)

# sum.example.py
s1 = sum([n**2 for n in range(10**6)])      # list comprehension
s2 = sum((n**2 for n in range(10**6)))      # generator wiht extra parenthesis
s3 = sum(n**2 for n in range(10**6))        # generator

# sum.example.py
s = sum([n**2 for n in range(10**9)])   # this is killed
# s = sum(n**2 for n in range(10 **9))  # this succeeds
print(s)  # prints: 33333333833333333500000000

# performance.py
from time import time
mx =5000
t = time() # start time for the for loop
floop = []
for a in range(1, mx):
    for b in range(a, mx):
        floop.append(divmod(a, b))
print('for loop: {:.4f} s'.format(time() - t))  # elapsed time 
t = time()  # start time for the list comprehension
compr = [
    divmod(a, b) for a in range(1, mx) for b in range(a, mx)]
print('list comprehension: {:.4f}s'.format(time() - t))
t = time()  # start time for the generator expression
gener = list(
    divmod(a, b) for a in range(1, mx) for b in range(a, mx))
print('generator expression: {:.4f} s'.format(time() - t))

# performance.map.py
from time import time
mx = 2 * 10 ** 7
t = time()
absloop = []
for n in range(mx):
    absloop.append(abs(n))
print('for loop: {:.4f} s'.format(time() - t))
t = time()
abslist = [abs(n) for n in range(mx)]
print('list comprehension: {:.4f}s',format(time() - t))
t = time()
absmap = list(map(abs, range(mx)))
print('map: {:.4f} s'.format(time() - t))

# functions.py
def gcd(a, b):
    """Calculate the Greatest Common Divisor of (a, b). """
    while b != 0:
        a, b = b, a % b
    return a 

# pythagorean.triple.generation.py
#from functions import gcd
N = 50
triples = sorted(
# 1  
    ((a, b, c) for a, b, c in (
# 2
        (( m**2 - n**2), (2 * m * n), (m**2 + n**2))    # 3 
        for m in range(1, int(N**.5) + 1)   #4
        for n in range(1, m)        # 5
        if (m-n) % 2 and gcd(m, n) == 1
    ) if c <= N), key=sum    
)

# pythagorean.triple.generation.for.py
#from functions import gcd
def gen_triples(N):
    for m in range(1, int(N**.5) + 1):  # 1
        for n in range(1, m):   # 2
            if (m - n) % 2 and gcd(m, n) == 1:  # 3
                c = m**2 + n**2     # 4
                if c <= N:     # 5
                    a = m**2 - n**2   # 6
                    b = 2 * m * n     # 7
                    yield (a, b, c)   # 8
                    sorted(gen_triples(50), key=sum)  # 9

# scopes.py
A = 100
ex1 = [A for A in range(5)]
print(A)   # prints: 100
ex2 = list(A for A in range(5))
print(A)   # prints: 100
ex3 = {A: 2 * A for A in range(5)}
print(A)   # prints: 100
ex4 = {A for A in range(5)}
print(A)   # prints: 100
s = 0
for A in range(5):
    s += A
print(A)   # prints: 4

# scopes.nonglobal.py
ex1 = [A for A in range(5)]
print(A)   # breaks: NameError: name 'A' is not defined

# scopes.for.py
s = 0 
for A in range(5):
    s += A
print(A)   # prints: 4
print(globals())  

# fibonacci first.py
def fibonacci(N):
    """Return all fibonacci numbers up to N. """
    result = [0]
    next_n = 1
    while next_n <= N:
        result.append(next_n)
        next_n = sum(result[-2:])
    return result
print(fibonacci(0))     # [0]
print(fibonacci(1))     # [0, 1, 1]
print(fibonacci(50))    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# fibonacci.second.py
def fibonacci(N):
    """Return all fibonacci numbers up to N. """
    yield 0
    if N == 0:
        return
    a = 0
    b = 1
    while b <= N:
        yield b
        a, b = b, a + b

# fibonacci.elegant.py
def fibonacci(N):
    """Return all fibonacci numbers up to N. """
    a, b = 0, 1
    while a <= N:
        yield a 
        a, b = b, a + b
