
fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

fruit_data = {}

for fruit in fruits:
    letter = fruit[0]
    if not letter in fruit_data:  # if fruit not already in dict
        fruit_data[letter] = []   # initialize empty list 
    fruit_data[letter].append(fruit)

for letter, fruit_list in fruit_data.items():
    print(letter, fruit_list)
