from collections import namedtuple

Person = namedtuple("Person", "first_name last_name")

p1 = Person('Frank', 'Sinatra')

p2 = Person(last_name="Martin", first_name="Dean")

print(f"p1.first_name: {p1.first_name}")
print(f"p2.last_name: {p2.last_name}")
