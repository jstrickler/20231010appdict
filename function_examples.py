def bark():
    print("woof! woof!")

bark()

def get_message():
    return "Happy October"

m = get_message()
print(f"m: {m}")

def boring():
    x = 5

b = boring()
print(f"b: {b}")

def display_message():
    msg = get_message()
    print(msg)

display_message()


def get_first_field(text, delimiter=':'):
    fields = text.split(delimiter)
    return fields[0]


print(f"get_first_field('foo-bar-blah', '-') {get_first_field('foo-bar-blah', '-')}")

# x = get_first_field(5, 25)

x = get_first_field(text="tra,la,la", delimiter=",")

print(f"get_first_field('apple:banana:mango'): {get_first_field('apple:banana:mango')}")

#      |  required   |
#       posonly    pos   opt  named      optional-named
def wacky(p1, /, p2, p3, *p4, p5, p6, p7, **p8):
    for k, v in p8.items():
        print(k, v)


my_args = {'animal': 'pine marten', 'country': 'Burkina Faso'}
wacky(5, 10, 15, 'a', 'b', 'c', p5=20, p6=25, p7=30, animal="wombat", country="Moldova")
wacky(5, 10, 15, 'a', 'b', 'c', p5=20, p6=25, p7=30, **my_args)



def doit(*files):
    for file in files:
        print(f"doing file {file}")

doit('foo.txt', 'bar.txt', 'blah.txt')
doit()

