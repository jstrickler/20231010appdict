
fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

for fruit in fruits:  # fruits is a collection (AKA container) -- contains values
    print(fruit)
print()

for fruit in reversed(fruits):  # reversed() returns an iterator
    print(fruit)
print()

for i, fruit in enumerate(fruits):  # enumerate() returns an iterator
    print(i, fruit)
print()

g = (f.upper() for f in fruits)
for fruit in g:
    print(fruit)
print()

#  fruits reversed(fruits) enumerate(fruits) g

