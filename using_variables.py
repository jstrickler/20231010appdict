
x = 5   #   int x = int(5);
y  = x  #  

#  a-z 0-9 _  A-Z 

# conventional_variable_name

# cnum BAD
# customer_number GOOD
#  CustomerNumber  GO BACK TO JAVA

# CustomerAccount OK for CLASSES
# MAX_TRIES OK for GLOBALS

gOnUt3 = 123

a = "apple"  # create new object
b = a # b refers to same object that a refers to

del a   # remove reference 'a' ('b' still exists)

print(f"b: {b}")


def spam(arg):
    print(arg)

spam(b)

thing = None

# animal
print(f"thing: {thing}")

