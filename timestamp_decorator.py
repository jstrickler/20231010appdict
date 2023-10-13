import logging
import time
from random import randint
from datetime import datetime
from functools import wraps

logging.basicConfig(
    filename="timestamps.log",
    level=logging.INFO,
)

def log_timestamp(original_function):

    @wraps(original_function)
    def replacement_function(*args, **kwargs):
        log_message = f"{original_function.__name__} called at {datetime.now().ctime()}"
        logging.info(log_message)

        result = original_function(*args, **kwargs)
        return result

    return replacement_function

@log_timestamp
def scream(x, y, z):
    time.sleep(randint(1, 3))
    print('AAAAIIIIIEEEEEEEEEEEEE')
    print(x, y, z)
    return 100

@log_timestamp
def head():
    print("MY HEAD IS EXPLODING!")
# head = log_timestamp(head)

for i in range(5):
    scream(1, 2, 3)
for i in range(3):
    head()
scream(55, 95, "wombat")

print(scream.__name__)
print(head.__name__)

