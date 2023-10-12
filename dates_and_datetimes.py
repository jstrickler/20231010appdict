from datetime import date, datetime
from time import time

now_unix = time()  #   number of seconds/microseconds since 1/1/70
print(f"now_unix: {now_unix}")

bill_gates_birthday = date(1955, 10, 28)
print(f"bill_gates_birthday: {bill_gates_birthday}")
print(f"bill_gates_birthday.month: {bill_gates_birthday.month}")

today = date.today()
print(f"today: {today}")

now = datetime.now()
print(f"now: {now}")

converted_time = datetime.fromtimestamp(now_unix)
print(f"converted_time: {converted_time}")

print(f"now.strftime('%x-%X'): {now.strftime('%x-%X')}")
print(f"now.strftime('%B %d'): {now.strftime('%B %d')}")
