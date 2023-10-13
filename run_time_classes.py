
class Animal:
    def __init__(self):
        self._is_alive = True
    

    @property
    def is_alive(self):
        return self._is_alive

    @is_alive.setter
    def is_alive(self, value):
        self._is_alive = value

animals = ['Dog', 'Bear', 'Tiger', 'Koala']

g = globals()

for animal in animals:
    g[animal] = type(animal, (Animal,), {})

# type("classname", (base classes, ...), {attributes})

d = Dog()
print(f"d: {d}")
print(f"d.is_alive: {d.is_alive}")

k = Koala()
print(f"k: {k}")
print(f"k.is_alive: {k.is_alive}")

Beagle = type('Beagle', (Dog,), {})
b = Beagle()
print(f"b: {b}")

