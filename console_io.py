person = "Jimmy Carter"
city = "Plains GA"
value = 38.32830323

print(person)
print(city)
print(value)
print()

print(person, city)
#  sys.stdout.write(str(person) + ' ' + str(city) + '\n')

print(person, value, city)

print(person, city, sep="/")
print(person, value, sep="==>")
print(person, city, value, sep=", ")
print(person, end=' ')
# if blah blah
print(city)
# else
# print other thing

print(city + ': ' + person)

print(f"{city}: {person}")  # f-string     f"blah"   f'blah' f"""blah"""  f'''blah'''
print(f"{person} lives in {city}")
print(f"The value is {value}")

print(f"the value is {value:.2f}")

bignum = 38293898333
print(f"bignum: {bignum:,d}")

user_name = input("What is your name? ")
print(f"Welcome, {user_name}")






