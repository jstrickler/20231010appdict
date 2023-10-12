
abbr = ['NC', 'TX', 'VA', 'PA', 'SC']

capitals = ['Raleigh', 'Austin', 'Richmond', 'Harrisburg']

combo = zip(abbr, capitals)

for name, cap in combo:
    print(name, cap)
print()
print(list(zip(abbr, capitals)))

