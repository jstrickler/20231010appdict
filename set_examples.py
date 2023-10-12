list1 = ['red', 'blue', 'red', 'green', 'purple', 'white', 'blue', 'brown']
list2 = ['blue', 'blue', 'brown', 'orange', 'pink', 'red', 'purple']

set1 = set(list1)
set2 = set(list2)

set1.add('black')
set2.add('yellow')

print(f"set1: {set1}")
print(f"set2: {set2}\n")

print("COMMON:", set1 & set2)   # intersection
print("NOT COMMON:", set1 ^ set2)  # xor
print("ALL:", set1 | set2)  # union

print("ONLY set1:", set1 - set2)
print("ONLY set2:", set2 - set1)

for color in 'turquoise', 'red', 'scarlet', 'blue', 'purple', 'lime green':
    print(color, color in (set1 | set2))

with open('DATA/breakfast.txt') as br_in:
    all_foods = br_in.read().splitlines()
unique_foods = set(all_foods)
print(f"unique_foods: {unique_foods}")
print(f"len(unique_foods): {len(unique_foods)}")
