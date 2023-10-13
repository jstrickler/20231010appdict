from functools import cache
from random import randint
from my_package.geometry import circle_area

# decorate circle_area with the cache decorator
circle_area = cache(circle_area)

for _ in range(10000):  # call circle_area() 10000 times
    result = circle_area(randint(1, 50))   # call with argument in range 1-50

print(circle_area.cache_info())  # show cache hits and misses

