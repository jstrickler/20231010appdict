
x = ['a', 'b', 'c']  

print(f"dir(x): {dir(x)}")
print(f"hasattr(x, '__iter__'): {hasattr(x, '__iter__')}")  # x HAS an iterator
print(f"hasattr(x, '__next__'): {hasattr(x, '__next__')}")  # x IS NOT an iterator, but it IS an iterable

# value = next(x)  INVALID

ix = iter(x)
print(f"hasattr(ix, '__iter__'): {hasattr(ix, '__iter__')}")  # x HAS an iterator, and IS an iterable
print(f"hasattr(ix, '__next__'): {hasattr(ix, '__next__')}")  # x IS an iterator

value = next(ix)
print(f"value: {value}")
value = next(ix)
print(f"value: {value}")

with open('DATA/mary.txt') as mary_in:
    header_lines = next(mary_in)
    print(f"header_lines: {header_lines}")
    
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)

ee = enumerate(x)
value = next(ee)
print(f"value: {value}")

