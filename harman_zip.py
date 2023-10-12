import os

FRUIT1 = "DATA/fruit1.txt"
FRUIT2 = "DATA/fruit2.txt"
# fruit_sets = {}

# with open(FRUIT1, "r") as f1, open(FRUIT2, "r") as f2:
#     for f1_line, f2_line in zip(f1, f2):
#         fruit1_set.add(f1.readline().rstrip().lower())
#         fruit2_set.add(f2.readline().rstrip().lower())  
#print(fruit1_set, fruit2_set)   
for file_path in FRUIT1, FRUIT2:
    file_name = os.path.basename(file_path)
    with open(file_path) as fruits_in:
        for line in fruits_in:
            fruit_sets[file_name].add(line.rstrip().lower())

print(fruit_sets)



print(fruit1_set - fruit2_set)
print(fruit1_set & fruit2_set)