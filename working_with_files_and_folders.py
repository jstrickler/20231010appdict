import os
from datetime import datetime

FOLDER = "DATA"
FILE_NAME = "alice.txt"

file_path = os.path.join(FOLDER, FILE_NAME)
print(f"file_path: {file_path}")

print(f"os.path.exists(file_path): {os.path.exists(file_path)}")

file_size = os.path.getsize(file_path)
print(f"file_size: {file_size}")
folder = os.path.dirname(file_path)
base = os.path.basename(file_path)
print(folder, base)
print(f"os.path.abspath(file_path): {os.path.abspath(file_path)}")
print(f"os.path.split(file_path): {os.path.split(file_path)}")
print(f"os.path.splitext(file_path): {os.path.splitext(file_path)}")
# os.path.splitdrive()  windows only

mod_ts = os.path.getmtime(file_path)
print(f"mod_ts: {mod_ts}")
file_mod_timestamp = datetime.fromtimestamp(mod_ts)
print(f"file_mod_timestamp: {file_mod_timestamp}")

access_ts = os.path.getatime(file_path)
print(f"access_ts: {access_ts}")
file_access_timestamp = datetime.fromtimestamp(access_ts)
print(f"file_access_timestamp: {file_access_timestamp}")
print()

FOLDER = 'SETUP'
setup_files = os.listdir(FOLDER)
print(f"setup_files: {setup_files}")
for file_name in setup_files:
    file_path = os.path.join(FOLDER, file_name)
    file_size = os.path.getsize(file_path)
    print(f"{file_size:6d} {file_name}")
print('-' * 60)

for entry in os.scandir(FOLDER):
    file_path = entry.path
    file_size = os.path.getsize(entry.path)
    print(f"{file_size:6d} {entry.name}, {entry.stat()}")
