import sys

list1 = list()   # new empty list
list2 = ['orange', 'purple', 'navy']
print(f"list2: {list2}")
print(f"len(list2): {len(list2)}")
print(f"list2[0]: {list2[0]}")
list3 = []   # new empty list

data = 'John:Smith:Denver:CO'
fields = data.split(':')
print(f"fields: {fields}")
print(f"fields[2]: {fields[2]}")
print(f"fields[-1]: {fields[-1]}")
print()

cities = ["San Antonio", "Boston", "Birmingham", "Atlanta", "Alexandria"]

print(f"len(cities): {len(cities)}")
print(f"cities[0]: {cities[0]}")
print(f"cities[-1]: {cities[-1]}")
print()

cities.insert(0, "Denver")
cities.insert(5, "Durham")
print(f"cities: {cities}")
cities.append("Plains")
cities.append("Fairfax")
cities.append("Reston")
print(f"cities: {cities}")

more_cities = ['Annandale', 'Clifton', 'Tysons Corner']
cities.extend(more_cities)   # for city in more_cities: cities.append(city)
print(f"cities: {cities}") 

cities[5] = "Raleigh"
print(f"cities: {cities}")

#  LIST.insert(pos, obj)    LIST.append(obj)   LIST.extend(iterable) 

pos = cities.index('Plains')
print(f"pos: {pos}")
del cities[pos]

cities.remove('Raleigh')  #  del cities.index("Raleigh")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}")

city = cities.pop(6)
print(f"city: {city}")
print(f"cities: {cities}")

#  del LIST[pos]    LIST.remove(value)   value = LIST.pop()  value = LIST.pop(pos)


fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

#   SEQUENCE[start=0:stop=len(SEQUENCE):step]
print(f"fruits[0:8]: {fruits[0:8]}")
print(f"fruits[4:8]: {fruits[4:8]}")
print(f"fruits[:3]: {fruits[:3]}")
print(f"fruits[1:]: {fruits[1:]}")
print()

print(f"sys.argv: {sys.argv}")
print(f"sys.argv[1:]: {sys.argv[1:]}")
args = sys.argv[1:]  # skip the script name

print(f"fruits[:-1]: {fruits[:-1]}")
print(f"fruits[1:-1]: {fruits[1:-1]}")  # omit last and last elements

city = 'Alexandria'
print(f"city[:4]: {city[:4]}")
print(f"city[4:7]: {city[4:7]}")
print(f"city[-4:]: {city[-4:]}")

print(f"cities: {cities}")
print()
for city in cities:
    print(city.upper())
print()
for letter in city:
    print(letter)
print()




