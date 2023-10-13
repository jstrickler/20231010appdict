from functools import wraps

# to implement a decorator as a class which takes arguments, __call__ RETURNS the replacement

class multiply:
    def __init__(self, multiplier):  # accept parameters
        self._multiplier = multiplier
    
    def __call__(self, orig_function):  # __call__ RETURNS the replacement function

        @wraps(orig_function)
        def replacement_function(*args, **kwargs):
            result = orig_function(*args, **kwargs)
            return result * self._multiplier
        return replacement_function

if __name__ == "__main__":
    
    @multiply(2)
    def spam():
        return 5
    #  spam = multiply(2)(spam)

    @multiply(10)
    def ham():
        return 8

    print(spam())
    print(spam())
    print(ham())
    print(spam())
    print(ham())
    print(ham())