fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

with open('fruits.txt', 'w') as fruits_out:
    for i, fruit in enumerate(fruits, 1):
        fruits_out.write(f"{i}#{fruit.title()}\n")   # or  f"{fruit}\n"

