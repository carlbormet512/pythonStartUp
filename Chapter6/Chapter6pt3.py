# oop/simplest.class.py
from wsgiref.handlers import format_date_time


class Simplest():  # when empty, the parenthesis are optional
    pass
print(type(Simplest))  # what type is this object
simp = Simplest()  # we create an instance of Simplest: simp
print(type(simp))  # what type is simp
# is simp an instance of Simplest?
print(type(simp) is Simplest)   # there's a better way to do this

# oop/class.namespaces.py
class Person:
    species = 'Human'
print(Person.species)   # Human
Person.alive = True   # Added dynamically
print(Person.alive)   # true
man = Person()
print(man.species)   # human (inherited)
print(man.alive)   # True (inherited)
Person.alive = False
print(man.alive)    # false(inherited)
man.name = 'Darth'
man.surname = 'Vader'
print(man.name, man.surname)   # Darth Vader

# oop/class.attribute.shadowing.py
class Point:
    x = 10
    y = 7
p = Point()
print(p.x)  # 10 (from class attribute)
print(p.y)  # 7  (from class attribute)
p.x = 12  # p gets its own 'x' attribute
print(p.x)  # 12  (now found on the instance)
print(Point.x)  # 10  (class attribute still the same)
del p.x  # we delete instance attribute
print(p.x)   # 10 (now search has tp go again to find class attr)
p.z = 3  # let's male it a 3D point
# print(p.z)   # 3
# print(Point.z)
#  Attribute error: type object point has no attribute 'z'

# oop/class.self.py
class Square:
    side = 8
    def area(self):  # self is a referance to an instance
        return self.side ** 2
sq = Square()
print(sq.area())  # 64 (side is found on the class)
print(Square.area(sq))   # 64  (equivalent to the previous line)
sq.side = 10
print(sq.area())  # 100 (side is found on the instance)

# oop/class.price.py
class Price:
    def final_price(self, vat, discount=0):
        """Returns price after applying vat and fixed discount."""
        return (self.net_price *(100 + vat)  / 100) - discount
p1 = Price()
p1.net_price = 100
print(Price.final_price(p1, 20, 10))   # 110 (100 * 1.2 - 10)
print(p1.final_price(20, 10))  # equivalent

# oop/class.init.py
class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    def area(self):
        return self.side_a * self.side_b
r1 = Rectangle(10, 4)
print(r1.side_a, r1.side_b)   # 10 4
print(r1.area())  # 40
r2 = Rectangle(7, 3)
print(r2.area())  # 21

# oop/class_inheritance.py
class Engine:
    def start(self):
        pass
    def stop(self):
        pass
class ElectricEngine(Engine):  # Is-A Engine
    pass
class V8Engine(Engine):  # Is-A Engine
    pass
class Car:
    engine_cls = Engine
    def __init__(self):
        self.engine = self.engine_cls()  # Has-A engine
    def start(self):
        print(
            'Starting engine {0} for car {1}... Wroom, wroom!'
            .format(
                self.engine.__class__.__name__,
                self.__class__.__name__
                )
            )
        self.engine.start()
    def stop(self):
        self.engine.stop()
class RaceCar(Car):  # Is-A Car
    engine_cls = V8Engine
class CityCar(Car):  # is a car
    engine_cls = ElectricEngine
class F1Car(RaceCar):  # Is-A RaceCar and also Is-A Car
    pass  # engine class same as parent
car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()
cars = [car, racecar, citycar, f1car]
for car in cars:
    car.start()

# oop/class.issubclass.isinstance.py
#  from class_inheritance import Car, RaceCar, F1Car
#  car = Car()
#  racecar = Racecar()
#  f1car = F1Car()
#  cars = [(car, 'car'), (racecar, 'racecar'), (f1car, 'f1car')]
#  car_classes = [Car, Racecar, F1Car]
#  for car, car_name in cars:
#      for class_ in car_classes:
#          belongs = isinstance(car, class_)
#          msg = 'is a' if belongs else 'is not a'
#          print(car_name, msg, class_.__name__)

# oop/class.issubclass.isinstance.py
#  for class1 in car_classes:
#      for class2 in car_classes
#          is_subclass = issubclass(class1, class2)
#          msg = '{0} a subclass of'.format(
#             'is' if is_subclass else 'is not')
#          print(class1.__name__, msg, class2.__name__)

# oop/super.duplication.py
class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages
class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        self.title = title
        self.publisher = publisher
        self.pages = pages
        self.format_ = format_

# oop/super.explicit.py
class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages
class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        Book.__init__(self, title, publisher, pages)
        self.format_ = format_
ebook = Ebook(
    'Learn Python Programming', 'Packt Publishing', 500, 'PDF')
print(ebook.title)  # Learn Python Programming
print(ebook.publisher)  # Packt Publishing

# oop/super.implicit.py
class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages
class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        super().__init__(title, publisher, pages)
        # Another way to do the same thing is:
        # super(Ebook, self).__init__(title, publisher, pages)
        self.format_ = format_
ebook = Ebook(
    'Learn Python Programming', 'Packt Publishing', 500, 'PDF')

# oop/multiple.inheritance.py
class Shape:
    geometric_type = 'Generic Shape'
    def area(self):  # This acts as placeholder for the interface
        raise NotImplementedError
    def get_geometric_type(self):
        return self.geometric_type
class Plotter:
    def plot(self, ratio, topleft):
        # Imagine there is some nice plotting logic here
        print('Plotting at {}, ratio {},',format(
            topleft, ratio))
class Polygon(Shape, Plotter):  # base class for polygons
    geometric_type = 'Polygon'
class RegularPolygon(Polygon):   # is a polygon
    geometric_type = 'Regular Polygon'
    def __init__(self , side):
        self.side = side
class RegularHexagon(RegularPolygon):   # is a regular polygon
    geometric_type = 'Regular Hexagon'
    def area(self): 
        return 1.5 * (3 ** .5 * self.side ** 2)
class Square(RegularPolygon):  # is a Regular Polygon
    geometric_type = 'Square'
    def area(self):
        return self.side * self.side
hexagon = RegularHexagon(10)
print(hexagon.area())     # 259.808
print(hexagon.get_geometric_type())    # RegularHexagon
hexagon.plot(0.8, (75, 77))   # Plotting at (75, 77), ratio 0.8.
square = Square(12)
print(square.area())  # 144
print(square.get_geometric_type())  # Square
square.plot(0.93, (74, 75))  # Plotting at (74, 75), ratio 0.93.

# oop/multiple.inheritance.py
print(square.__class__.__mor__)
# prints:
#  (<class '__main__.Square'>,<class '__main__.RegularPolygon'>, 
# <class '__main__.Polygon'>, <class '__main__.Shape'>,
# <class ' __main__.Plotter'>, <class 'object'>)

# oop/mro.simple.py
class A:
    label = 'a'
class B(A):
    label = 'b'
class C(A):
    label = 'c'
class D(B, C):
    pass
d = D()
print(d.label) # hypothetically it could be b or c

# oop/mro.py
class A:
    label = 'a'
class B(A):
    pass
class C(A):
    label = 'c'
class D(B, C):
    pass
d = D()
print(d.label)  # 'c'
print(d.__class__.mro())  

# oop/static.methods.py
class StringUtil:
    @staticmethod
    def is_palindrome(s, case_insensitive=True):
        # we aallow only letter and numbers
        s = ''.join(c for c in s if c.isalnum())
        # for case insensitive comparisson, we lower-case s
        if case_insensitive:
            s = s.lower()
        for c in range(len(s))  // 2:
            if s[c] != s[-c -1]:
                return False
        return True
    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())
print(StringUtil.is_palindrome('Radar', case_insensitive=False))  #  False: Case Sensitive
print(StringUtil.is_palindrome('A nut for a jar of tuna'))  # True
print(StringUtil.is_palindrome('Never Odd, Or Even!')) # True
print(StringUtil.is_palindrome(
    'In Girum Imus Nocte Et Consumimur Igni'))   # True
print(StringUtil.get_unique_words(
    'I love palindromes. I really really love them!'))
#  {'them!', 'palindromes.', 'I', 'really', 'love'}

