from pprint import pprint

FILE_NAME = "DATA/knights.txt"

knight_info = {}

with open(FILE_NAME) as file_in:
    for raw_line in file_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment =  line.split(':')
        knight_info[name] = title, color, quest, comment

pprint(knight_info)
print()

for name, data in knight_info.items():
    print(data[0], name, data[2])
print()

print(f"knight_info['Robin'][2]: {knight_info['Robin'][2]}")

