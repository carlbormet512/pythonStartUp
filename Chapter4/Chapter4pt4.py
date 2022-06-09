# parameters.defaults.mutable.py
def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a)) # this affects a's default value
    b[len(a)] = len(a)  # and this will affect b's
func()
func()
func()

# parameters.defaults,mutable.intermediate.call.py
func()
func(a=[1, 2, 3], b={'B': 1})
func()

# parameters.defaults.mutable.no.trap.py
def func(a=None):
    if a is None:
        a = []
        # do whatever you want with 'a' 

# return.none.py
def func():
    pass
func()  # the return of this call won't be collected. it's lost
a = func()  # the return of this one instead is collected into  'a'
print(a) # prints: None

# return.single.value.py
def factorial(n):
    if n in(0, 1):
        return 1
    result = n 
    for k in range(2, n):
        result *= k
    return result
f5 = factorial(5)  # f5 = 120

# return.single.value.2.py
from functools import reduce
from operator import mul
def factorial(n):
    return reduce(mul, range(1, n + 1), 1)
f5 = factorial(5)   #  = 120

# return.multiple.py
def moddiv(a, b):
    return a // b, a % b
print(moddiv(20, 7))  # prints (2, 6)

# recursive.factorial.py
def factorial(n):
    if n in (0, 1):   # base case
        return 1
    return factorial(n - 1) * n  # recursive case

# filter.regular.py
def is_multiple_of_five(n):
    return not n % 5
def get_mulyiples_of_five(n):
    return list(filter(is_multiple_of_five, range(n)))

# filter.lambda.py
def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))

# lambda.explained.py
# example 1: adder
def adder(a, b):
    return a + b
# is equvilant to:
adder_lambda = lambda a, b: a + b# example 2: to uppercase
def to_upper(s):
    return s.upper()
# is equivilant to:
to_upper_lambda = lambda s: s.upper()

# func.attributes.py
def multiplication(a, b=1):
    """Return a multiplied by b."""
    return a * b
if __name__ == "__main__":
    special_attributes = [
        "__doc__", "__name__", 
        "__qualname__", "__module__",
        "__defaults__", "__code__", "__globals__", 
        "__dict__", "__closure__", "__annotations__", 
        "__kwdefaults__",
    ]
    for attribute in special_attributes:
        print(attribute, '->', getattr(multiplication, attribute))