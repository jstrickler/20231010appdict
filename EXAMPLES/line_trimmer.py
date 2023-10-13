def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            # this yield line effectively is the __next__() method in the generator
            yield line.rstrip('\n\r')  # 'yield' causes this function to return a generator object (__next__)

mary_in = trimmed('../DATA/mary.txt')
for trimmed_line in mary_in:
    print(trimmed_line)
