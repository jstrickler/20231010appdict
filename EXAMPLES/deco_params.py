#

from functools import wraps  # wrapper to preserve properties of original function


def multiply(multiplier): # actual decorator -- receives decorator parameters

    def deco(old_func): # "inner decorator" -- receives function being decorated

        @wraps(old_func)  # retain name, etc. of original function
        def replacement_for_original_function(*args, **kwargs): # replacement function -- this is called instead of original
            result = old_func(*args, **kwargs) # call original function and get return value
            if isinstance(result, (int, float, str, list, tuple, bytes)):
                return result * multiplier # multiple result of original function by multiplier
            else:
                raise TypeError(f"Unable to multiply type {type(result).__name__}")

        return replacement_for_original_function # deco() returns new_function

    return deco # multiply returns deco



@multiply(4)
def spam():
    return 5
# spam = multiply(4)(spam)

inner_deco = multiply(4)   # multiply(...) returns deco()
spam = inner_deco(spam)    # inner_deco is really deco()


@multiply(10)
def ham():
    return 10



a = spam()
b = ham()
print(a, b)


# @alpha
# def foo():
#     pass

# foo = alpha(foo)

# @beta(1, 2, 3)
# def bar():
#     pass

# bar = beta(1, 2, 3)(bar)

deco5 = multiply(5) 

@deco5
def apple():
    return 'a'

def banana():
    return 'b'
banana = deco5(banana)

@deco5
def cherry():
    return 'c'

print(apple())
print(banana())
print(apple())
print(apple())
print(cherry())
print(banana())
