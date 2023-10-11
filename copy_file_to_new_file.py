
input_file = "DATA/presidents.txt"
output_file = "mavericks.txt"

with open(input_file) as pres_in:
    with open(output_file, "w") as pres_out:
        for raw_line in pres_in:
            line = raw_line.rstrip() # strip \n
            term, last_name, first_name, dob, dod, bplace, bstate, took, left, party = line.split(':')
            if (party != 'Democratic') and (party != 'Republican'):
                pres_out.write(f"{first_name}|{last_name}|{party}\n")
        