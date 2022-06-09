# docstings.py
def square(n):
    """Return the square of a number n. """
    return n ** 2
def get_username(userid):
    """Return the username of a user given their id."""
    return
"""db.get(user_id=userid).username"""

# imports.py
from datetime import datetime, timezone 
from unittest.mock import patch
#import pytest 
#from core.models import  (
#    Exam,
#    Exercise,
#    Solution,
#)

# lib/funcdef.py
def square(n):
    return n ** 2
def cube(n):
    return n ** 3
 
# func_import.py
#import lib.funcdef
#print(lib.funcdef.square(10))
#print(lib.funcdef.cube(10))

# func_from.py
#from lib.funcdef import square, cube
print(square(10))
print(cube(10))

# primes.py
from math import sqrt, ceil
def get_primes(n):
    """Calculate a list of primes up to n (included). """
    primelist = []
    for candidate in range(2, n + 1):
        is_prime = True
        root = ceil(sqrt(candidate))   # division limit
        for prime in primelist:  # we try only the primes
            if prime > root:    # no need to check any further
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primelist.append(candidate)
    return primelist