#discount.py
from datetime import date, timedelta
today = date.today()
tomorrow = today + timedelta(days = 1)
products = [
    {'sku':'1', 'expiration_date': today, 'price': 100.0},
    {'sku': '2', 'expiration_date': tomorrow, 'price': 50}, 
    {'sku': '3', 'expiration_date': today, 'price': 20},
]
for product in products:
    if product['expiration_date'] != today:
        continue
    product['price'] *= 0.8
    print(
        'Price for sku', product['sku'], 'is now', product['price'])


#any.py
items = [0, None, 0.0, True, 0, 7]
found = False
for item in items:
    print('scanning item', item)
    if item:
        found = True
        break
if found: 
    print('At least one of the item evaluates to True')
else:
    print('All items evaluate to False')

#for.no.else.py
class DriverException(Exception):
    pass
people = [('James', 17), ('Kirk', 9), ('Lars', 13), ('Robert', 8)]
driver = None
for person, age in people:
    if age >= 18:
        driver = (person, age)
        break
if driver is None:
    raise DriverException('Driver not found.')


#or
#for.else.py
class DriverException(Exception):
    pass
people = [('James', 17), ('Kirk', 9), ('Lars', 13), ('Robert', 8)]
for person, age in people:
    if age >= 18:
        driver = (person, age)
        break
else:
    raise DriverException('Driver not found')




# menu.no.walrus.py
flavors = ["pistachia", "malaga", "vanilla", "chocolate", "strawberry"]
prompt = "Choose your flavor: "
print(flavors)
while True:
    choice = input(prompt)
    if choice in flavors:
        break
    print(f"Sorry, '{choice}' is not a valid option.")
    print(f"You chose '{choice}'.")

#menu.wlarus.py
flavors = ["pistachio", "malaga", "vanilla", "chocolate", "strawberry"]
prompt = "Choose your flavor: "
print(flavors)
#while (choice := input(prompt))
#not in flavors:
#    print(f"Sorry, '{choice}' is not a valid option.")
#    print(f"You chose'{choice}'.")