

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

nums = [800, 80, 1000, 32, -4, 255, -8, 400, 5, 5000]

print(f"len(fruits): {len(fruits)}")
print(f"len(fruits[0]): {len(fruits[0])}")
print(f"len(nums): {len(nums)}\n")

print(f"min(fruits): {min(fruits)}")
print(f"min(nums): {min(nums)}\n")

print(f"sum(nums): {sum(nums)}\n")

print(f"sorted(fruits): {sorted(fruits)}")
print(f"sorted(nums): {sorted(nums)}\n")

x = ['apple', 'banana', 'cherry']

rx = reversed(x)
print(f"rx: {rx}")
for thing in rx:
    print(thing)
print()

for i, fruit in enumerate(fruits, 1):
    print(i, fruit)
print('-' * 60)

e = enumerate(fruits)
print(f"e: {e}\n")
print(f"list(e): {list(e)}\n")
print(f"list(e): {list(e)}")







