from pprint import pprint

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"dir(fruits): {dir(fruits)}")

clear = getattr(fruits, 'clear')
print(f"clear: {clear}")
clear()
print(f"fruits: {fruits}")
print(f"hasattr(fruits, '__iter__'): {hasattr(fruits, '__iter__')}")

class Dog:
    pass

def bark(self):
    print("woof woof woof")

d = Dog()

setattr(Dog, 'bark', bark)

d.bark()

delattr(Dog, 'bark')

# d.bark()



