"""
String examples

simple examples of Python string usage
"""

s1 = "spam\n"    # 5 chars
s2 = 'spam\n'    # 5 chars
s3 = r"spam\n"  # raw string   also r'spam\n' 
print(f"s2: {s2}")
print(f"s3: {s3}")

s4 = """spam\n"""
s5 = '''spam\n'''

print("63\u00B0 in Durham")

print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')

print("""Guido's the ex-"BDFL" of Python""")   # triple-quoted strings

query = """
select *
from customers
where state = 'OH'
order by balance desc
limit 50
"""





