import sys
import sqlite3
import logging

# smtp_handler = logging.handlers.SMTPHandler(...)
# syslog_handler = logging.handlers.SysLogHandler(...)
logging.basicConfig(
    filename="blech.log",
    level=logging.INFO,
    format="%(levelname)s %(name)s %(filename)s %(asctime)s %(message)s",
    datefmt="%x-%X",
    # handlers=[smtp_handler]
)


file_path = "DATA/wombats.txt"
logging.info("opening %s", file_path)

try:
    with open(file_path) as wombats_in:
        pass
    print("continuing")
except (FileNotFoundError, PermissionError) as err:
    logging.exception(err)
except OSError as err:
    logging.error("UH-OH", err)
except Exception as err:
    logging.error("Not an OS Error!", err)

nums = [800, 80, 1000, 0, 32, -4, 255, -8, 0, 400, 5, 5000]

for num in nums:
    try:
        result = 5000 / num
    except ZeroDivisionError as err:
        logging.warning(err)
        # exit nicely
        # sys.exit(1)  # exit with error code
    else:  # if no exceptions
        print(f"result: {result}")

print("ALL DONE")


conn = None

try:
    db_name = '/australia/wombat.db'
    logging.debug("connecting to %s", db_name)
    conn = sqlite3.connect(db_name)
except (sqlite3.DatabaseError, sqlite3.OperationalError) as err:
    logging.error(err)
    sys.exit(1)
else:
    cursor = conn.cursor()
    # execute SQL here ...
finally:
    if conn is not None:
        conn.close()




