# oop/class.methods.factory.py
from argparse import ArgumentDefaultsHelpFormatter
import py_compile


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @classmethod
    def from_tuple(cls, coords):
# cls is Point
        return cls(*coords)
    @classmethod
    def from_point(cls, point):
# cls is Point
        return cls(point.x, point.y)
p = Point.from_tuple((3, 7))
print(p.x, p.y)  # 3 7
q = Point.from_point(p)
print(q.x, q.y)  # 3 7

# oop/class.methods.split.py
class StringUtil:
    @classmethod
    def is_palindrome(cls, s, case_insensitive=True):
        s = cls._strip_string(s)
        # For case insensitive comparison, we lower-case s
        if case_insensitive:
            s = s.lower()
        return cls._is_palindrome(s)
    @staticmethod
    def _strip_string(s):
        return ''.join(c for c in s if c.isalnum())
    @staticmethod
    def _is_palindrome(s):
        for c in range(len(s) // 2):
            if s[c] != s[-c -1]:
                return False
        return True
    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())
print(StringUtil.is_palindrome('A nut for a jar of tuna'))   # True
print(StringUtil.is_palindrome('A nut for a jar of beans'))   # False

# oop/private.attrs.py
class A:
    def __init__(self, factor):
        self._factor = factor
    def op1(self):
        print('Op1 with facotr{}...'.format(self._factor))
class B(A):
    def op2(self, factor):
        self._factor = factor
        print('Op2 with factor{}...'.format(self._factor))
obj = B(100)
obj.op1()   # Op1 with factor 100...
obj.op2(42)   # Op2 with factor 42...
obj.op1()    # Op1 with factor 42...

# oop/private.attrs.fixed.py
class A:
    def __init__(self, factor):
        self.__factor = factor
    def op1(self):
        print('Op1 with factor{}...'.format(self.__factor))
class B(A):
    def op2(self, factor):
        self.__factor = factor
        print('Op2 with factor {}...'.format(self.__factor))
obj = B(100)
obj.op1()    # op1 with factor 100
obj.op2(42)  # op2 with factor 42
obj.op1()    # op1 with factor 100

# oop/property.py
class Person:
    def __init__(self, age):
        self.age = age  # anyone can modify this freely
class PersonWithAccessors:
    def __init__(self, age):
        self.age = age
    def get_age(self):
        return self.age
    def set_age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18, 99]')
class PersonPythonic:
    def __init__(self, age):
        self.age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18, 99]')
person = PersonPythonic(39)
print(person.age)  # 39 - Notice we access as data attribute
person.age = 42   # Motice we access as data attribute
print(person.age)  # 42
person.age = 100  # Value Error

# Example.py
class Client:
    def __init__(self):
        print("Setting up the client...")
    def query(self, **kwargs):
        print(f"Performing a query: {kwargs}")
class Manager:
    @property
    def client(self):
        return Client()
    def preform_query(self, **kwargs):
        return self.client.query(**kwargs)

# Example.2.py
class ManuelCacheManager:
    @property
    def client(self):
        if not hasattr(self, '_client'):
            self._client = Client()
        return self._client

# Example.3.py
from functools import cached_property
class CachedPropertyManager:
    @cached_property
    def client(self):
        return Client()
    def preform_query(self, **kwargs):
        return self.client.query(**kwargs)
manager = CachedPropertyManager()
manager.preform_query(object_id=42)
manager.preform_query(name_ilike='%Python%')
del manager.client # This causes a new client on next call
manager.preform_query(age_gte=18)

# oop/operator.overloading.py
class Weird:
    def __init__(self, s):
        self._s = s
    def __len__(self):
        return len(self._s)
    def __bool__(self):
        return '42' in self._s
weird2 = Weird('Hello! I am 42 years old!')
print(len(weird2))   # 25
print(bool(weird2))   # True

# oop/dataclass.py
from dataclasses import dataclass
@dataclass
class Body:
    '''Class to represent a aphysical body.'''
    name: str
    mass: float = 0.  # Kg
    speed: float = 1.   # m/s
    def kinetic_energy(self) -> float:
        return (self.mass * self.speed **2) / 2
body = Body('Ball', 19, 3.1415)
print(body.kinetic_energy())  # 93.756 Joule
print(body)   # Body(name='Ball', mass=19, speed=3.1415)

# iterators/iterator.py
class OddEven:
    def __init__(self, data):
        self._data = data
        self.indexes = (list(range(0, len(data), 2)) + list(range(1, len(data), 2)))
    def __iter__(self):
        return self
    def __next__(self):
        if self.indexes:
            return self._data[self.indexes.pop(0)]
        raise StopIteration
oddeven = OddEven('ThIsIsCoOl!')
print(''.join(c for c in oddeven))  # TIICO!hssol
oddeven = OddEven('CiAo')  # or manually
it = iter(oddeven)  # this calls oddeven.__iter__ internally
print(next(it))  # C
print(next(it))  # A
print(next(it))  # i
print(next(it))  # o

