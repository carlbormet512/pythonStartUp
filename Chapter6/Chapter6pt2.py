# decorators/time.measure.deco2.py
from time import sleep, time
from functools import wraps
def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
    return wrapper
@measure
def f(sleep_time=0.1):
    """I'm a cat. I love to sleep!"""
    sleep(sleep_time)
    f(sleep_time=0.3)   # f took: 3.00
    print(f.__name__, ':', f.__doc__)   # f : I'm a cat. I love to sleep!

# decoractors/two.decorators.py
from time import time
from functools import wraps
def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
        return result
    return wrapper
def max_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 100:
            print(
                f'Result is too big  ({result}). '
                'Max allowed is 100.'
            )
        return result
    return wrapper
@measure
@max_result
def cube(n):
    return n ** 3
    print(cube(2))
    print(cube(5))

# decorators/decorators.factory.py
from functools import wraps
def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(
                    f'Result is too big({result}), '
                    f'Max allowed id {threshold}.'
                )
            return result
        return wrapper
    return decorator
@max_result(75)
def cube(n):
    return n ** 3
print(cube(5))


