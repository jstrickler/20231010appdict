d1 = dict()   # empty dictionary
d2 = {'m': 8, 'z': 10, 'r': 15}
d3 = {}  # empty dictionary
d4 = dict(m=8, z=10, r=15)

data = [('m', 8), ('z', 10), ('r', 15)]
d5 = dict(data) 

print(f"d2 == d4 == d5: {d2 == d4 == d5}")

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

airports['PHX'] = 'Phoenix'
airports['DCA'] = "Washington, DC"
airports['ORD'] = "Chicago"

print(f"airports: {airports}")

print(f"airports['LHR']: {airports['LHR']}")
# print(f"airports['SAT']: {airports['SAT']}")
# print(f"airports['AUS']: {airports['AUS']}")
print(f"airports.get('SAT'): {airports.get('SAT')}")
print(f"airports.get('IAD'): {airports.get('IAD')}")
print(f"airports.get('AUS', 'Austin'): {airports.get('AUS', 'Austin')}")

print(f"airports.setdefault('AUS', 'Austin'): {airports.setdefault('AUS', 'Austin')}")
print(f"airports: {airports}")

del airports['MCO']
print()
print(f"airports: {airports}")
print()

for code, city in airports.items():
    print(code, city)
print('-' * 60)

for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)

print(f"airports.items(): {airports.items()}")


def sort_by_value(element):
    return element[1], element[0]

for code, city in sorted(airports.items(), key=sort_by_value):
    print(code, city)
print('-' * 60)
