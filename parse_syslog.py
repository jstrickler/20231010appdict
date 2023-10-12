from syslog_parser import SyslogParser

sp = SyslogParser('/var/log/system.log')

for entry in sp: 
    if entry['process_name'] == 'McAfee: ':
        print(entry['message'])