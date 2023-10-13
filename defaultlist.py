
class DefaultList(list):
    def __init__(self, default_function):
        self._default_function = default_function

    def __getitem__(self, index):     # LIST[n]
        if index > len(self):
            return self._default_function()
        else:
            return super().__getitem__(index)


if __name__ == "__main__":
    def get_none():
        return None

    dl = DefaultList(get_none)
    dl.append('a')
    dl.append('b')
    print(f"dl[0]: {dl[0]}")
    print(f"dl[99]: {dl[99]}")
    print(f"dl[1]: {dl[1]}")
    
    d2 = DefaultList(lambda : 0)
    fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
    'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
    'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
    'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]
    
    for f in fruits:
        d2.append(f)

    print(f"d2: {d2}")
    print(f"d2[0]: {d2[0]}")
    print(f"d2[-1]: {d2[-1]}")
    print(f"d2[23534]: {d2[23534]}")
    
    