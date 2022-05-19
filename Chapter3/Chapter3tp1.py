#taxes.py
income = 150000000000
if income < 10000:
    tax_coefficient = 0.0
elif income < 30000:
    tax_coefficient = 0.2
elif income < 100000:
    tax_coefficient = 0.35
else:
    tax_coefficient = 0.45

print(f'You will pay: ${income * tax_coefficient} in taxes')

