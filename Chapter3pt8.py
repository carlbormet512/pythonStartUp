#primes.py
primes = []
upto = 100 
for n in range(2, upto +1):
    is_prime = True
    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            break
    if is_prime: 
        primes.append(n)
print(primes)

#primes.else.py
primes = []
upto = 100
for n in range(2, upto + 1):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)
print(primes)



#switch.py
#if 1 <= day_number <= 5:
#    day = 'Weekday'
#elif day_number == 6:
#    day = 'Saturday'
#elif day_number == 0:
#    day = 'Sunday'
#else:
#    day = ''
#    raise ValueError(str(day_number) + ' is not a valid day number.')


#coupons.py
customers = [
    dict(id=1, total=200, coupon_code='F20'), 

    dict(id=2, total =150, coupon_code='P30'), 

    dict(id=3, total=100, coupon_code='P50'), 

    dict(id=4, total=110, coupon_code='F15'), 
]
for customer in customers:
    code = customer['coupon_code']
    if code == 'F20':
        customer['discount'] = 20.0
    elif code == 'F15':
        customer['discount'] = 15.0
    elif code == 'P30':
        customer['discount'] = customer['total'] * 0.3
    elif code == 'P50':
        customer['discount'] = customer['total'] * 0.5
    else:
        customer['discount'] = 0.0
for customer in customers:
        print(customer['id'], customer['total'], customer['discount'])



#coupons.dict.py
customers = [
    dict(id = 1, total = 200, coupon_code ='F20'), 
    dict(id=2, total=150, coupon_code='P30'), 
    dict(id=3, total=100, coupon_code='P50'),
    dict(id=4, total=110, coupon_code='F15')
]
discounts = {
    'F20': (0.0, 20.0),
    'P30': (0.3, 0.0),
    'P50': (0.5, 0.0),
    'F15': (0.0, 15.0),
}
for customer in customers:
    code = customer['coupon_code']
    percent, fixed = discounts.get(code, (0.0, 0.0))
    customer['discount'] = percent * customer['total'] + fixed
for customer in customers:
    print(customer['id'], customer['total'], customer['discount'])
