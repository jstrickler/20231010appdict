
colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']


for color in colors:   # like 'foreach' in some languages
    print(color)
print()

#  for VAR in ANY_ITERABLE:
#      ... VAR ... 

while True:  # loop 'forever'
    name = input("Name? ")
    if name == 'q':
        break  # exit loop NOW
    if name == '':
        continue  # go back to condition
    favorite_color = input("Favorite color? ")
    print(f"{name}'s favorite color is {favorite_color}")
print(f"colors: {colors}")

for i, color in enumerate(colors):
    if i == 1:
        print(color)

print(colors[6])
print(colors[2:5])   #    LIST[start:stop]    


# Bad python:
# i = 0
# while i < len(colors):
#     print(colors[i])
#     i += 1 

