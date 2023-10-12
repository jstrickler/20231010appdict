with open("../DATA/fruit1.txt") as fruit1_in:
    fruits = fruit1_in.read().lower().splitlines()
    fruit1 = set(fruits)

with open("../DATA/fruit2.txt") as fruit2_in:
    fruits = fruit2_in.read().lower().splitlines()
    fruit2 = set(fruits)

common_fruits = fruit1 & fruit2

print(common_fruits)
