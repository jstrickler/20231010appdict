
file_path = "DATA/breakfast.txt"

food_counts = {}

with open(file_path) as food_in:
    for raw_line in food_in:
        food = raw_line.rstrip()
        if not food in food_counts:
            food_counts[food] = 0  # initialize value for this key
        food_counts[food] += 1  # add one to current value and then overwrite with new value

for food, count in food_counts.items():
    print(food, count)

