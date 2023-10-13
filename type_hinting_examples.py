import typing as T

Number = T.Union[int, float]

def spam(name: str, value: Number) -> float:
    print(f"name: {name}   value: {value}")
    return 42.9


spam("Bob", 25)
spam("Margie", 32.6)

spam(33, 93)
spam('foo', 'bar')

def find_lines(search_term: str, file_list: T.Iterable[str]) -> list[str]:
    # for file_path in file_list:
    #     print(file_path)
    return []


find_lines('bird', ['alice.txt', 'parrot.txt', 'mary.txt'])
find_lines('bird', ('alice.txt', 'parrot.txt', 'mary.txt'))
files = ['alice.txt', 'parrot.txt', 'mary.txt']
find_lines('bird', reversed(files))

find_lines('bird', 234)

