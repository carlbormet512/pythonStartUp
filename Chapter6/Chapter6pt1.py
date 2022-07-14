# decorators/time.measure.start.py
from email.utils import decode_rfc2231
from time import sleep, time
def f():
    sleep(.3)
def g():
    sleep(.5)
t = time()
f()
print('f took:', time() - t)
t = time()
g()
print('g took:', time() - t)

# decorators/time.measure.dry.py
from time import sleep, time
def f():
    sleep(.3)
def g():
    sleep(.5)
def measure(func):
    t = time()
    func()
    print(func.__name__, 'took:', time() - t)
measure(f)
measure(g)

# decorators/time.measure.arguements.py
from time import sleep, time
def f(sleep_time=0.1):
    sleep(sleep_time)
def measure(func, *args, **kwargs):
    t = time()
    func(*args, **kwargs)
    print(func.__name__, 'took:', time() - t)
measure(f, sleep_time=0.3)
measure(f, 0.2)

# decorators/time.measure.deco1.py
from time import sleep, time
def f(sleep_time=0.1):
    sleep(sleep_time)
def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
    return wrapper
f = measure(f)   # decoration point
f(0.2) 
f(sleep_time=0.3)
print(f.__name__)

# decorators/syntax.py
def func(arg1, arg2):
    pass
# func = decorator(func) 
 # is equivalent to the following
# @decorator
def func(arg1, arg2):
    pass

# decorators/syntax.py
def func(arg1, arg2):
    pass
# func = deco1(deco2(func))
# is equvalent to the following:
# @deco1 
# @deco2 
def func(arg1, arg2):
    pass

# decorators/syntax.py
def func(arg1, arg2):
    pass
# func = decoarg(arg_a, arg_b)
(func)
# is eqivalent to the following
# @decoarg(arg_a, arg_b)
def func(arg1, arg2):
    pass