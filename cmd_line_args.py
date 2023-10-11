import sys

print(f"sys.argv: {sys.argv}")

if len(sys.argv) > 1:
    print(f"sys.argv[1]: {sys.argv[1]}")
else:
    print("Please specify arg on the cmd line")

# convert nums with
#  float(s)  int(s)

value = 56
if value > 75:
    print("wombat")
    print("wallaby")
elif value > 50:   # else if
    print('kangaroo')
    print('quokka')
else:
    print('platypus')
    print('blue-ringed octopus')

print("ALL DONE")


