from rundeco import add_run

class Animal:
    pass

@add_run
class Dog(Animal):
    def bark(self):
        print("woof woof")

class Cat(Animal):
    pass


d = Dog()
d.run()