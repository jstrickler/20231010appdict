from pprint import pprint

color = "Green"
cities = ['Pittsburgh', 'Durham', 'Miami']
value = 123

print(f"dir(cities): {dir(cities)}")
print('-' * 60)

g = globals()
pprint(g)
print('-' * 60)

print(f"__name__: {__name__}")
print(f"__file__: {__file__}")

print(f"g['color']: {g['color']}")

g['animal'] = "wombat"

print(f"animal: {animal}")  
pprint(g)

def spam(p1, p2):
    name = "Mary"
    print(f"locals(): {locals()}")
    
spam('a', 5)
print()



