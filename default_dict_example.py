from collections import defaultdict
from pprint import pprint


x = {}

# print(f"x['wombat']: {x['wombat']}")
print(f"x.get('wombat', 'NO ANIMAL'): {x.get('wombat', 'NO ANIMAL')}")

#   dd = defaultdict(FUNC)

def zero():
    return 0

#               callback!
dd = defaultdict(zero)   # pass in function which returns default value

dd['honey badger'] = 5
dd['pine marten'] = 10

print(f"dd['honey badger']: {dd['honey badger']}")
print(f"dd['wombat']: {dd['wombat']}")

print(f"dd: {dd}")

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

fruits_by_first_letter = defaultdict(list)

for fruit in fruits:
    letter = fruit[0]
    fruits_by_first_letter[letter].append(fruit)

pprint(fruits_by_first_letter)

