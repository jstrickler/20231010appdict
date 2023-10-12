import sys
from my_package import geometry   # find geometry.py and execute the code

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

print(geometry.DUCKS)

# looks in sys.path, created from:
# 
# 1. current folder
# 2. folders from PYTHONPATH  env variable
# 3. folders from sys.prefix/lib
print(f"sys.prefix: {sys.prefix}\n")
for path in sys.path:
    print(path)


