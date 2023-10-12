from my_local_module import useful_function1, useful_function2

FILE_PATH = "/var/log/system.log"

with open(FILE_PATH) as log_in:
    for raw_line in log_in:
        if 'failed' in raw_line.lower():
            line = raw_line.rstrip()
            if 'ProcMonitor' in line:
                useful_function1()
            elif 'Wombat' in line:
                useful_function()
            else:
                raise Exception("I don't know what to do")
            #  parse info from log entry
            #  modify info as needed
            #  call useful_function(info....)

