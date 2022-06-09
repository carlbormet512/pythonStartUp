#matrix.multiplication.nofunc.py
a = [[1, 2], [3, 4]]
b = [[5, 1], [2, 1]]
c = [[sum(i * j for i, j in zip(r, c)) for c in zip( *b)] 
    for r in a]

#matrix.multiplication.func.py
def matrix_mul(a, b):
    return [[sum(i*j for i, j in zip(r, c))for c in zip(*b)]
        for r in a]
a = [[1, 2], [3, 4]]
b = [[5, 1], [2, 1]]
c = matrix_mul(a, b)


# vat.py
price = 100  #GBP, no VAT
final_price1 = price* 1.2
final_price2 = price + price / 5.0
final_price3 = price * (100 + 20) / 100.0
final_price4 = price + price * 0.2

# vat.function.py
def calculate_price_with_vat(price, vat):
    return price * (100 + vat) / 100


# scoping.level.1.py
def my_function():
#    test = 1 # this is defined in the local scope of the function
    print('my_function:', test)
test = 0 # this is defined in the global scope
my_function()
print('global:', test)

# scoping.level.2.py
def outer():
    #test = 1 # outer scope
    def inner():
    #    test = 2 # inner scope
        print('inner:', test)
    inner()
    print('outer:', test)
test = 0 # global scope
outer()
print('global:', test) 

# scoping.level.2.nonlocal.py
def outer():
    test = 1 # outer scope
    def inner():
        nonlocal test
        test = 2 # nearest enclosing scope (which is 'outer')

        print('inner:', test)
    inner()
    print('outer:', test)
test = 0 # global scope
outer()
print('global:', test)

# scoping.level.2.global.py
def outer():
    test = 1 # outer scope
    def inner():
        global test 
        test = 2 # global scope
        print('inner:', test)
    inner()
    print('outer:', test)
test = 0 # global scope
outer()
print('global:', test)