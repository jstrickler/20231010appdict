from collections import Counter

# c = Counter(iterable)
# 
# c = Counter()
# c[key] += 1

file_path = "DATA/breakfast.txt"

with open(file_path) as breakfast_in:
    foods = breakfast_in.read().splitlines()  # read file into a list of lines without newlines

food_counts = Counter(foods)
print(f"food_counts: {food_counts}")
