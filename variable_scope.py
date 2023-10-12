

name = "Otto"  # global variable

def spam():
    # global name     naughty programmer!!
    name = "Brenda"  # local variable

spam()

print(f"name: {name}")

