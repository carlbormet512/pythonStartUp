# exceptions/first.example.py    For the Command line
# gen = (n for n in range(2))
# next(gen)
#  0
# next(gen)
#  1
# next(gen)
#  Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
#  StopIteration
# print(undefined_name)
#  Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
#  NameError: name 'undefined_name' is not defined
# mylist = [1, 2, 3]
# mylist[5]
#  Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
#  IndexError: list index out of range
# mydict = {'a': 'A', 'b': 'B'}
# my dict['c']
#  Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
#  KeyError: 'c'
# 1 / 0
#  Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
#  ZeroDivisionError: division by zero

# exceptions/unhandles.py
1 + "one"
print("this line will never be reached")

# exceptions/raising.py   Command Line
# raise NotImpplementedError("I'm afriad I can't do that")
#  Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
#  NotImplementedError: I'm afraid I can't do that

# Exceptions/trace.back.py
def squareroot(number):
    if number < 0:
        raise ValueError("No negative numbers please")
    if number % 2 == True:
        raise ValueError("No even numbers please")
    return number ** .5

def quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    return ((-b - squareroot(d)) / (2 * a), (-b + squareroot(d)) / (2 * a))
quadratic(1, 0, 1)  # x**2 + 1 == 0

# exceptions/try.syntax.py
def try_syntax(numerator, denominator):
    try:
        print(f'In the try block: {numerator}/{denominator}')
        result = numerator / denominator
    except ZeroDivisionError as zde:
        print(zde)
    else:
        print('The result is:', result)
        return result
    finally:
        print('Exiting')
print(try_syntax(12, 4))
print(try_syntax(11, 0))

# exception/multiple.py
values = (1, 2)
try:
    q, r = divmod(*values)
except (ZeroDivisionError, TypeError) as e:
    print(type(e), e)

# exceptions/multiple.py
try:
    q, r = divmod(*values)
except ZeroDivisionError:
    print("You tried to divide by zero!")
except TypeError as e:
    print(e)

# exceptions/for.loop.py
n = 100
found = False
for a in range(n):
    if found: break
    for b in range(n):
        if found: break
        for c in range(n):
            if 42 * a + 17 * b + c == 5096:
                found = True
                print(a, b, c)  # 79 99 95

# exceptions/for.loop.py
class ExitLoopException(Exception):
    pass

try:
    n = 100
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if 42 * a + 17 * b + c == 5096:
                    raise ExitLoopException(a, b, c)
except ExitLoopException as ele:
    print(ele.args)  # (79, 99, 95)

# context/deciaml.prec.py
from decimal import Context, Decimal, getcontext, setcontext
one = Decimal("1")
three = Decimal("3")
orig_ctx = getcontext()
ctx = Context(prec=5)
setcontext(ctx)
print(ctx)
print(one / three)
setcontext(orig_ctx)
print(one / three)

# context/decimal.prec.py
orig_ctx = getcontext()
ctx = Context(prec=5)
setcontext(ctx)
try:
    print(ctx)
    print(one / three)
finally:
    setcontext(orig_ctx)
print(one / three)

# context/decimal.prec.py
from decimal import localcontext
with localcontext(Context(prec=5)) as ctx:
    print(ctx)
    print(one / three)
print(one / three)

# context/decimal.prec.py
with localcontext(Context(prec=5)), open("out.txt", "w") as out_f:
    out_f.write(f"{one} / {three} = {one / three}\n")

# context/manager.class.py
class MyContextManager:
    def __init__(self):
        print("MyContextManager init", id(self))
    def __enter__(self):
        print("Entering 'with' context")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{exc_type=} {exc_val=} {exc_tb=}")
        print("Exiting 'with' context")
        return True

# context/manager.class.py
ctx_mgr = MyContextManager()
print("About to enter 'wtih' context")
with ctx_mgr as mgr:
    print("Inside 'with' context")
    print(id(mgr))
    raise Exception("Exception inside 'with' context")
    print("This line will never be reached")
print("After 'with' context")
