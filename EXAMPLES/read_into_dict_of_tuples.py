from pprint import pprint

FILE_NAME = "../DATA/knights.txt"

def main():
    data = get_data()
    pretty(data)
    print()
    print_details(data)
    print()
    print(get_field(data, 'Robin', 2))

def get_data():
    knight_info = {}  # create empty dict

    with open(FILE_NAME) as knights_in:
        for line in knights_in:
            name, title, color, quest, comment = line.rstrip('\n\r').split(":")
            knight_info[name] = title, color, quest, comment  # create new dict element with name as key and a tuple of the other fields as the value
    return knight_info

def pretty(info):
    pprint(info)

def print_details(knight_info):
    for name, fields in knight_info.items():
        print(fields[0], name)

def get_field(knight_info, knight, field_number):
    return knight_info[knight][field_number]

main()