#paramaters.default.py
def func(a, b=4, c=88):
    print(a, b, c)
func(1)     #prints 1 4 88
func(b=5, a=7, c=9)     #prints 7 5 9
func(42, c=9)       #prints 42 4 9
func(42, 43, 44)        #prints 42 43 44

# parameters.variable.positional.py
def minimum(*n):
    #print(type(n))   # n is a tuple
    if n:  
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)
minimum(1, 3, -7, 9)  # n = (1, 3, -7, 9) - prints: -7
minimum()   # n = ()  - prints: nothing

# parameters.variable.keyword.py
def func(**kwargs):
    print(kwargs)
func(a=1, b=42) # prints: {'a': 1, 'b': 42}
func() # prints {}
func(a=1, b=46, c=99)   # prints {'a': 1, 'b': 46, 'c': 99}

# parameters.positional.only.py
def func(a, b, /, c):
    print(a, b, c)
func(1, 2, 3)   # prints: 1 2 3
func(1, 2, c=3)   # prints: 1 2 3

# Parameters.positional.only.optional.py
def func(a, b=2, /):
    print(a, b)
func(4, 5)  # prints: 4 5
func(3) #prints: 3 2

# parameters.keyword.only.py
def kwo(*a, c):
    print(a, c)
kwo(1, 2, 3, c=7)   # prints:  (1, 2, 3) 7
kwo(c=4)    # prints: () 4
# kwo(1, 2)   # breaks, invalid syntax
def kwo2(a, b=42, *, c):
    print(a, b, c)
kwo2(3, b=7, c=99)  # prints: 3 7 99
kwo2(3, c=13)  # prints: 3 42 13
# kwo2(3, 23) # breaks, invalid syntax

# parameters.all.py
def func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)
    print('args:', args)
    print('kwargs:', kwargs)
func(1, 2, 3, 5, 7, 9, A='a', B='b')

# parameters.all.pkwonly.py
def allparams(a, /, b, c=42, *args, d=256, e, **kwargs):
    print('a, b, b:', a, b, c)
    print('d, e:', d, e)
    print('args:', args)
    print('kwargs:', kwargs)
allparams(1, 3, 4, 4, 5, 6, e=7, f=9, g=10)

