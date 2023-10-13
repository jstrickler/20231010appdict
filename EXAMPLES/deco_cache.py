from functools import wraps

cache = {}

def silly_cache(orig_function):

    @wraps(orig_function)
    def replacement(*args):
        if args not in cache:
            cache[args] = orig_function(*args)
        return cache[args]

# something like
#    wraps(replacement, orig_function)

    return replacement


@silly_cache
def raise_to_power(a, b):
    print(f"params {a} {b}")
    return a ** b


print(raise_to_power.__name__)

for x, y in (1, 3), (4, 5), (1, 3), (2, 8), (1, 3):
    print(raise_to_power(x, y))

