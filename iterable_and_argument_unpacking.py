

data = ['Durham', 'NC']

city, state = data  # city = data[0]; state = data[1] ...
print(f"city: {city}   state: {state}")

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

for i, fruit in enumerate(fruits):
    print(i, fruit)
print(f"list(enumerate(fruits)): {list(enumerate(fruits))}")
print()

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', 'apple', 'mango', 'wombat', '1969-12-28'),
]

for first_name, last_name, *product, dob in people:
    print(last_name, product, dob)
print()

for first_name, last_name, *_ in people:
    print(first_name, last_name)
print('-' * 60)


def find_text(file_name, search_term):
    print(f"file_name: {file_name}   search_term: {search_term}")

find_text('DATA/mary.txt', 'pig')
find_text('hello.py', 'world')

search_term_list = [
    ('foo.txt', 'bar'),
    ('spam.txt', 'ham'),
    ('blah.txt', 'barf'),
]

for thing in search_term_list:
    find_text(*thing)  # unpack iterable into individual arguments
print('-' * 60)

for file_name, term in search_term_list:
    find_text(file_name, term)

    

