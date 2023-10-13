

def doit(func):

    def replacement_function(*args, **kwargs):
        print("SURPRISE!!")
        print("Extra functionality here...")
        result = func(*args, **kwargs)  # call original scream()
        return result  # return the return val of original scream()

    return replacement_function

@doit
def scream(x, y, z):
    print('AAAAIIIIIEEEEEEEEEEEEE')
    print(x, y, z)
    return 100

# scream is REPLACED with wrapper
# scream = doit(scream) # scream now refers to wrapper

m = scream('a', 'b', 'c')  # calling wrapper('a', 'b', 'c')
print(f"m: {m}")

@doit
def exploded_head():
    print("MY HEAD IS EXPLODING!")

# exploded_head = doit(exploded_head)
exploded_head()


